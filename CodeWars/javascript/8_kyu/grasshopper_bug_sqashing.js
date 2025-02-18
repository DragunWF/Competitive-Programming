// https://www.codewars.com/kata/56214b6864fe8813f1000019/train/javascript

var health = 100;
var position = 0;
var coins = 0;

function main() {
  rollDice();
  move();
  combat();
  getCoins();
  buyHealth();
  printStatus();
}

// Example functions (Not included in solution)
// Just some dump functions
function getCoins() {
  return coins;
}

function buyHealth() {
  if (coins >= 10) {
    coins -= 10;
    health += 25;
  }
}

function move() {
  position += 1;
}

function printStatus() {
  console.log(`Health: ${health}\nPosition: ${position}\nCoins: ${coins}`);
}

function combat() {
  health -= 15;
}

function rollDice() {
  const min = 1,
    max = 2;
  const randomRoll = Math.random() * (max - min) + min;
  if (randomRoll === 1) {
    health += 15;
    coins += 10;
  } else {
    health -= 10;
    coins -= 10;
  }
}

function attack() {
  coins += 10;
}
