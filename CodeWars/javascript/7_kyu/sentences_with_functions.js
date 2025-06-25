// https://www.codewars.com/kata/52567c56cb6ac86b56000516/train/javascript

function Adam(word) {
  return "Adam" + continuation(word);
}
function has(word) {
  return "has" + continuation(word);
}
function a(word) {
  return "a" + continuation(word);
}
function dog(word) {
  return "dog" + continuation(word);
}
function The(word) {
  return "The" + continuation(word);
}
function name(word) {
  return "name" + continuation(word);
}
function of(word) {
  return "of" + continuation(word);
}
function the(word) {
  return "the" + continuation(word);
}
function is(word) {
  return "is" + continuation(word);
}
function also(word) {
  return "also" + continuation(word);
}
function continuation(word) {
  return word ? ` ${word}` : ".";
}

// ========================

function test() {
  console.log(Adam(has()));
  console.log(has());
  console.log(Adam());
}

test();
