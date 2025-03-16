// https://www.codewars.com/kata/5143cc9694a24abcd2000001/train/javascript

Object.defineProperty(Array.prototype, "containsAll", {
  value: function containsAll(arr) {
    for (let i = 0; i < arr.length; i++) {
      if (!this.includes(arr[i])) {
        return false;
      }
    }
    return true;
  },
});
