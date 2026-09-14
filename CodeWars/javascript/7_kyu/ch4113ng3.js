// https://www.codewars.com/kata/59e9f404fc3c49ab24000112/train/javascript

function nerdify(txt) {
  const replacementMap = {
    e: "3",
    E: "3",
    a: "4",
    A: "4",
    l: "1",
  };
  let output = txt;
  for (let key of Object.keys(replacementMap)) {
    while (output.includes(key)) {
      output = output.replace(key, replacementMap[key]);
    }
  }
  return output;
}
