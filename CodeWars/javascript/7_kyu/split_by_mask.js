// https://www.codewars.com/kata/6a68ed7894f29599a1f7a248/train/javascript

function split(string, mask) {
  if (!string.length) {
    return !mask.length ? [] : null;
  }

  const output = [];
  let chunk = "";
  let currentMaskIndex = 0;
  let maskLengthSum = mask.reduce((a, b) => a + b, 0);
  let chunkLengthSum = 0;

  for (let char of string) {
    chunk += char;
    if (currentMaskIndex >= mask.length) {
      return null;
    }
    if (chunk.length >= mask[currentMaskIndex]) {
      chunkLengthSum += chunk.length;
      currentMaskIndex++;
      output.push(chunk);
      chunk = "";
    }
  }

  return chunkLengthSum !== maskLengthSum ? null : output;
}
