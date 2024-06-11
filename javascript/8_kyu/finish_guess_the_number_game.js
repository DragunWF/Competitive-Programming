// https://www.codewars.com/kata/568018a64f35f0c613000054/train/javascript

class Guesser {
  constructor(number, lives) {
    this.number = number;
    this.lives = lives;
  }

  guess(n) {
    if (this.lives <= 0) throw new Error();
    if (n === this.number) return true;
    this.lives--;
    return false;
  }
}
