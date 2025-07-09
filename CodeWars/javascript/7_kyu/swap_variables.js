// https://www.codewars.com/kata/586ed14c35396d912100049a/train/javascript

swap = (ary) => {
  ary[0] = ary[0] ^ ary[1];
  ary[1] = ary[0] ^ ary[1];
  ary[0] = ary[0] ^ ary[1];
};
