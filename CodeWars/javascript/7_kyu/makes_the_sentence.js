// https://www.codewars.com/kata/59fb4d89ff58e5e816002efc/train/javascript

function makesTheSentence(characterArray, sentenceString) {
  const sentenceCharactersArray = sentenceString
    .split("")
    .filter((item) => item != " ");
  characterArray.sort();
  sentenceCharactersArray.sort();
  return characterArray.join("") == sentenceCharactersArray.join("");
}

function test() {
  console.log(
    makesTheSentence(
      ["D", "u", "c", "k", "s", "q", "u", "a", "c", "k", "."],
      "Ducks quack."
    ) // true
  );
}

test();
