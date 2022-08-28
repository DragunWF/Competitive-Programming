// https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/javascript

function getPINs(observed) {
  const keys = getPossibleKeys(observed);
  if (keys.length === 1) return keys[0];

  const possiblePINs = [];
  let combination = "";
  for (let i = 0; i < observed.length; i++) {
    for (let keySet of keys) {
      for (let key of keySet) {
        if (i == 0) possiblePINs.push(key);
        else possiblePINs[i] += key;
      }
    }
  }

  return possiblePINs;
}

function getPossibleKeys(observed) {
  const output = [];
  const subtractors = [0, 1, -1, 3, -3];
  for (let key of observed) {
    const possibleKeys = [];
    for (let num of subtractors) {
      const diff = key - num;
      if (diff > 0 && diff <= 9 && !output.includes(diff.toString()))
        possibleKeys.push(diff.toString());
    }
    if (key === "8") possibleKeys.push("0");
    output.push(possibleKeys);
  }
  return output;
}

console.log(getPINs("8"));
console.log(getPINs("11"));
console.log(getPINs("369"));
