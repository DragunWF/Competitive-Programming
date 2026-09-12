// https://www.codewars.com/kata/5a0efbb7c374cb69970000cf/train/javascript

function reverseMessage(str) {
  const reversed_sentence = [];
  const words = str.split(" ");
  words.reverse();

  for (let word of words) {
    const reversedWord = reverseString(word);

    if (reversedWord.length === 1) {
      reversed_sentence.push(reversedWord);
    } else {
      reversed_sentence.push(
        `${reversedWord.charAt(0).toUpperCase()}${reversedWord.substring(1).toLowerCase()}`,
      );
    }
  }

  return reversed_sentence.join(" ");
}

function reverseString(word) {
  let reversed = "";
  for (let char of word) {
    reversed = char + reversed;
  }
  return reversed;
}

function test() {
  console.log(reverseMessage("Reverse this message!"));
}

test();
