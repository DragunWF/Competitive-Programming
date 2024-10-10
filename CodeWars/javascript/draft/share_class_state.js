// https://www.codewars.com/kata/53583765d5493bfdf5001b35
// Drafted because I can't use ES6 for this kata

class Cat {
  static instances = [];

  constructor(name, weight) {
    this.name = name;
    this.weight = weight;
    Cat.instances.push(this);
  }

  static averageWeight() {
    let sum = 0;
    for (let object of this.instances) {
      sum += object.weight;
    }
    return sum / this.instances.length;
  }
}

// Not part of the solution
garfield = new Cat("garfield", 25);
console.log(Cat.averageWeight()); // 25

felix = new Cat("felix", 15);
console.log(Cat.averageWeight()); // now 20
