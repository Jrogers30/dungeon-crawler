from flask import Flask ,jsonify,request,render_template
from dungeon import Hero,Monster
import json,uuid,os


app = Flask(__name__)
games = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def save_hero(hero):
    data = hero.to_dict()
    path = os.path.join(BASE_DIR, "hero.json")
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

@app.route("/new_game", methods = ["POST"])

def new_game():
    game_id = str(uuid.uuid4())
    with open(os.path.join(BASE_DIR, "hero.json"), mode="r", encoding="utf-8") as file:
        hero_data = json.load(file)
    hero = Hero(hero_data["name"],hero_data["hp"],hero_data["attack"])

    with open(os.path.join(BASE_DIR, "monster.json"), mode="r", encoding="utf-8") as file:
        monster_data = json.load(file)    
    
    monsters = []

    for data in monster_data:
        monsters.append(
            Monster(data["name"],
                    data["hp"],
                    data["attack"]
                )
            )
    games[game_id] = {"hero": hero, "monsters": monsters}
    response = {
        "game_id": game_id,
        "hero": hero.to_dict(),
        "monster": monsters[0].to_dict()
    }
    return jsonify(response)


@app.route("/action", methods = ["POST"])

def action():
    data = request.get_json()
    game_id = data["game_id"]
    move = data["move"]

    game = games.get(game_id)
    
    if not game:
        return jsonify({"error": "game not found"}), 404
    
    hero = game["hero"]
    monster = game["monsters"][0]
    if move == "attack":
        hero.attack(monster)
    elif move == "defend":
        hero.defend()
    elif move == "quit":
        save_hero(hero)
        return jsonify({"result": "QUIT"})
    else:
        return jsonify({"error": "invalid move"}), 400
    
    if not monster.isalive():
        game["monsters"].pop(0)
        if len(game["monsters"]) == 0:
            return jsonify({"result": "WIN", "hero": hero.to_dict()})
        next_monster = game["monsters"][0]
        return jsonify({
            "result": "KILLED",
            "hero": hero.to_dict(),
            "monster": next_monster.to_dict()
        })
    monster.take_turn(hero)

    
    if not hero.isalive():
        return jsonify({"result": "HERO_DEAD", "hero": hero.to_dict(), "monster": monster.to_dict()})

   
    return jsonify({"result": "TURN", "hero": hero.to_dict(), "monster": monster.to_dict()})

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)