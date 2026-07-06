import random
import json

class Character:
    def __init__(self, name,hp,attackpwr):
        self.name = name
        self.hp = hp
        self.attackpwr = attackpwr
        self.defending = False
        


    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attackpwr}")
        target.takeDmg(self)

    
    
    def show_status(self):
        label = type(self).__name__
        return f"\n{label}: {self.name}\nHP: {self.hp}\nAttack: {self.attackpwr}\n"  
    
    def defend(self):
        self.defending = True

    def takeDmg(self, attacker):
        if self.defending:
            print("BLOCKED SOME DMG!")
            self.hp -= attacker.attackpwr // 2
            self.defending = False
        else:
           self.hp -= attacker.attackpwr
        
        return self.hp
    
    def isalive(self):
        return self.hp > 0
    


        
class Hero(Character):
    def __init__(self, name, hp, attackpwr):
        super().__init__(name, hp, attackpwr)
        
    def take_turn(self,opp):
        while True:
            user_input = input("\nCHOOSE: ATTACK or DEFEND or QUIT: ").lower()
            if user_input == "attack":
                
                self.attack(opp)
                return "TURN"
            elif user_input == "defend":
                self.defend()
                print(f"{self.name} is defending!")
                return "TURN"
            elif user_input == "quit":
                return "QUIT"
                
            else:
                print("TRY AGAIN!")

    
    
        
        


    
        
class Monster(Character):
    def take_turn(self,opp):
        turn = random.choices([1,2], weights=[.8,.2],k=1)
        if turn[0] == 1:
            self.attack(opp)
        elif turn[0] == 2:
            self.defend()
            print(f"{self.name} is defending!")
            
            
            

    



def fight(hero,monster):
    
    if hero.take_turn(monster) != "QUIT":
        res = monster.isalive()

        if not res:
            print("YOU HAVE KILLED THE MONSTER MOVING ON TO THE NEXT ONE\n")
            
            return "KILLED"
        
        monster.take_turn(hero)
        res = hero.isalive()
        if not res:
            print("YOU DIED BY MONSTER")
            return "HERO"
    else:
        return "QUIT"
   
        
    
   






with open ('hero.json', mode="r", encoding="utf-8") as file:
    hero_data = json.load(file)


with open ('monster.json', mode="r", encoding="utf-8") as file:
    monster_data = json.load(file)


hero = Hero(hero_data["name"],hero_data["hp"],hero_data["attack"])
monsters = []

for data in monster_data:
    monsters.append(
        Monster(data["name"],
                data["hp"],
                data["attack"]
            )
        )
    
monster = monsters[0]


def save(character):
    data = {
        "name": character.name,
        "hp": character.hp,
        "attack": character.attackpwr
    }
    with open ("hero.json", mode="w", encoding="utf-8") as file:
        json.dump(data,file,indent=2)

def save_monsters(data):
    list_of_monsters = []
    for monsters_obj in data:
        list_of_monsters.append({
            "name": monsters_obj.name,
            "hp": monsters_obj.hp,
            "attack": monsters_obj.attackpwr
        })
    with open ("monster.json", mode="w", encoding="utf-8") as file:
        json.dump(list_of_monsters,file,indent=2)
    
    


while True:


    print(f"{hero.show_status()}{monster.show_status()}")

    game_res = fight(hero,monster)
    if game_res == "QUIT":
        save(hero)
        save_monsters(monsters)
        break
    elif game_res == "KILLED":
        monsters.pop(0)
        save_monsters(monsters)
        if len(monsters) == 0:
            print("YOU HAVE BEATEN ALL THE MONSTERS!!!!")
            break

        monster = monsters[0]
    elif game_res == "HERO":
        break
    
    




#jake = Hero("jake",20,5)
#zombie = Monster("zombie",15,10)










'''
print(jake.defending) # False
print(jake.defend()) # True
print(jake.takeDmg(zombie)) #15
print(jake.defending) # False
'''
#print(zombie.attack(jake))
#








'''
hero_name = input("Enter your Heros name: ")

hero = { "name": hero_name, 
        "hp": 10,
        "attack": random.randrange(1,10),
        }
zombie = { "name": 'zombie', 
        "hp": 20,
        "attack": random.randrange(1,10)
        }
print(f"{hero['name']} has stepped into the dungeon with {hero['hp']} HP and {hero['attack']} attack")



print(f"{hero['name']} has appeared to find a wandering {zombie['name']}")   







def defend(hero_HP, mattk,defense):
    reduced = defense - mattk

    if reduced < 0:

       hero_HP += reduced
    else:
        print("You have defended against the attk\n")

    return hero_HP

def win_status(hero_hp, Mon_HP):
    win_status = False 
    if hero_hp <= 0:
        print("YOU LOST!!!")
        win_status = True
    elif Mon_HP <= 0:
        print("YOU WON!!!")
        win_status = True

    return win_status

def show_status():

    return f"\nHero: {hero['name']}\tMonster: {zombie['name']}\nHP: {hero['hp']}\t\tHP: {zombie['hp']}\nATK: {hero['attack']}\t\tATK: {zombie['attack']}"

def monster_turn(hero_HP, mattk):

    hero_HP -= mattk

    return hero_HP

def fight(hit_points,mhit_points,attk_pwr,mattk_pwr):
        

    print(show_status())
    user = input("CHOOSE: ATTACK or DEFEND").lower()
    if user == "attack":
        print(f"HERO {hero['name']} attacks {zombie['name']} for {hero['attack']} dmg.\n")
        mhit_points = attack(mhit_points,attk_pwr)

        print(f"MONSTER {zombie['name']} attacks {hero['name']} for {zombie['attack']} dmg.\n")
        hit_points = monster_turn(hit_points,mattk_pwr)

    elif user == "defend":

        hit_points = defend(hit_points,mattk_pwr,5)

    else:
        print("TRY AGAIN!\n")
    
    return hit_points,mhit_points
        




while True:

    hero['hp'],zombie['hp'] = fight(hero['hp'],zombie['hp'],hero['attack'],zombie['attack'])
    game_end = win_status(hero['hp'],zombie['hp'])
    if game_end == True:
        break
    hero['attack'] = random.randrange(1,10)
    zombie['attack'] = random.randrange(1,10)

'''