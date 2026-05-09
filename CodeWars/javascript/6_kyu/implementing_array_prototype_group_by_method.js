// https://www.codewars.com/kata/53c2c3e78d298dddda000460/train/javascript

Object.defineProperty(Array.prototype, "groupBy", {
  value: function groupBy(hashFunc) {
    const groups = {};
    for (let element of this) {
      const key = hashFunc ? hashFunc(element) : element;
      if (key in groups) {
        groups[key].push(element);
      } else {
        groups[key] = [element];
      }
    }
    return groups;
  },
});
