// https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/javascript

function parse(data) {
  const output = [];
  let value = 0;
  for (let char of data) {
    switch (char) {
      case "i":
        value++;
        break;
      case "d":
        value--;
        break;
      case "s":
        value *= value;
        break;
      case "o":
        output.push(value);
    }
  }
  return output;
}

console.log(parse("iiisdoso"));
