// https://www.codewars.com/kata/534fcca5edb124cfe6000f60/train/javascript

class Singleton {
  static instance;

  constructor() {
    if (Singleton.instance) {
      return Singleton.instance;
    }

    Singleton.instance = this;
  }
}
