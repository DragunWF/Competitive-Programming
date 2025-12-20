// https://www.codewars.com/kata/526471539d52735c620000c6/train/javascript

class Counter {
  constructor() {
    this.value = 0;
  }

  increase() {
    this.value++;
  }

  getValue() {
    return this.value;
  }

  reset() {
    this.value = 0;
  }
}
