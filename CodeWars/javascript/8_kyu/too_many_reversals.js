// https://www.codewars.com/kata/687de0b45ab74765f516ce3f/train/javascript

function whowon(s) {
  const wrestlers = s.split(" hit a reversal to ");
  return wrestlers[wrestlers.length - 2];
}
