// https://www.codewars.com/kata/5654d2428be803670a000030/train/javascript

function guessMyNumber(guess, number = "123-451-2345") {
  const output = [];
  for (let char of number) {
    if (guess.includes(char) || char === "-") {
      output.push(char);
    } else {
      output.push("#");
    }
  }
  return output.join("");
}
