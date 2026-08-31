// https://www.codewars.com/kata/53f211b159c3fcec3d000efa/train/javascript

function left$(str, i) {
  return process(str, i, true);
}

function right$(str, i) {
  return process(str, i, false);
}

function process(str, i, isLeft) {
  if (i === undefined) {
    i = 1;
  }

  const output = [];
  if (typeof i === "string") {
    if (!str.includes(i)) return "";

    let currentIndex = isLeft ? 0 : str.length - 1;
    let currentChar = str[currentIndex];
    if (isLeft) {
      let currentSubstring = str.substring(
        currentIndex,
        currentIndex - i.length,
      );
      while (currentSubstring !== i) {
        output.push(currentChar);
        currentIndex++;
        currentChar = str[currentIndex];
        currentSubstring = str.substring(currentIndex - i.length, currentIndex);
      }
    } else {
      let currentSubstring = null;
      while (currentSubstring !== i) {
        currentSubstring = str.substring(currentIndex - i.length, currentIndex);
        output.push(currentChar);
        currentIndex--;
        currentChar = str[currentIndex];
      }
    }
  } else {
    if (i < 0) {
      i += str.length;
    }
    if (isLeft) {
      for (let j = 0; j < i; j++) {
        output.push(str[j]);
      }
    } else {
      for (let j = str.length - 1, n = 0; n < i && j >= 0; j--, n++) {
        output.push(str[j]);
      }
    }
  }
  if (!isLeft) {
    output.reverse();
  }

  const outputStr = output.join("").trim();
  if (typeof i === "string") {
    return outputStr.replace(i, "");
  }
  return outputStr;
}

function test() {
  const text = "Hello (not so) cruel World!";

  // ##== with integer as 2nd argument ==
  console.log(left$(text, 5)); // # -> 'Hello'
  console.log(left$(text, -22)); // # -> 'Hello'
  console.log(left$(text, 1)); // # -> 'H'
  console.log(left$(text)); // # -> i defaults to 1
  console.log(left$(text, 0)); // # -> ''
  console.log(left$(text, 99)); // # -> 'Hello (not so) cruel World!'

  console.log(right$(text, 6)); // # -> 'World!'
  console.log(right$(text)); // # -> '!' (i defaults to 1)

  // #== with string as 2nd argument ==
  console.log(left$(text, "o")); // # -> 'Hell'
  console.log(right$(text, "o")); // # -> 'rld!'
  console.log(left$(text, " ")); // # -> 'Hello'
  console.log(left$(text, "xyz")); // # -> '' (substring not found)

  console.log(left$("Don't Repeat Yourself", "Repeat"));
}

test();
