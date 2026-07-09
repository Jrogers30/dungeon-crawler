let gameId = null;
let heroMaxHp = 1, monsterMaxHp = 1;


function show(id){ 
    document.getElementById(id).classList.remove('hidden'); 
}
function hide(id){ 
    document.getElementById(id).classList.add('hidden'); 
}
function log(msg){ 
    document.getElementById('log').textContent = msg;
}

function updateBars(hero, monster)
{
  document.getElementById('hero-name').textContent = hero.name;
  document.getElementById('hero-hp').textContent = hero.hp + ' HP';
  document.getElementById('hero-hp-bar').style.width = Math.max(0, hero.hp/heroMaxHp*100) + '%';
  if (monster)
  {
    document.getElementById('monster-name').textContent = monster.name;
    document.getElementById('monster-hp').textContent = monster.hp + ' HP';
    document.getElementById('monster-hp-bar').style.width = Math.max(0, monster.hp/monsterMaxHp*100) + '%';
  }
}

function endGame(message)
{
  hide('battle-screen');
  show('end-screen');
  document.getElementById('end-message').textContent = message;
}



async function startGame(){

    const response = await fetch('/new_game', { method: 'POST' });
    const data = await response.json();
    gameId = data.game_id;
    heroMaxHp = data.hero.hp
    monsterMaxHp = data.monster.hp
    hide('start-screen');
    show('battle-screen');
    updateBars(data.hero,data.monster);

}

async function sendAction(move){
    const response = await fetch('/action', {
        method : 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ game_id: gameId, move: move })
    });
    const data = await response.json();
    if (data.result === "TURN")
    {
        updateBars(data.hero, data.monster);
        log("ATTACKED!");
    } 
    else if (data.result === "KILLED")
    {
        monsterMaxHp = data.monster.hp;
        updateBars(data.hero, data.monster);
        log("Monster slain!");
    } 
    else if (data.result === "WIN")
    {
        endGame("YOU CLEARED THE DUNGEON!");
    } 
    else if (data.result === "HERO_DEAD")
    {
        endGame("YOU DIED.");
    } 
    else if (data.result === "QUIT")
    {
        endGame("You fled the dungeon.");
    }
    

}
