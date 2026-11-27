// https://www.codewars.com/kata/5313b713bb244a0eb20001fe/train/javascript

class Counter {
  constructor() {
    this.number = 0;
  }
  incr() {
    this.number++;
  }
  [Symbol.toPrimitive]() {
    return this.number;
  }
}
