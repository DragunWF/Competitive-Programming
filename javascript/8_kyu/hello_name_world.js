// https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/javascript

function hello(name) {
  if (!(typeof name === "string" && name.length)) return "Hello, World!";
  return `Hello, ${name[0].toUpperCase() + name.substring(1).toLowerCase()}!`;
}
