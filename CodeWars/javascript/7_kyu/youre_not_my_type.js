// https://www.codewars.com/kata/57157a7c2ad76331360002d0/train/javascript

Object.defineProperty(Array.prototype, "ofType", {
  value: function ofType(type) {
    const primitives = ["Boolean", "Number", "String"];
    return this.filter((item) => {
      if (primitives.includes(type.name)) {
        return typeof item === type.name.toLowerCase();
      }
      return item instanceof type;
    });
  },
});
