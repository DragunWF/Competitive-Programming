// https://www.codewars.com/kata/56747fd5cb988479af000028/train/javascript

function getMiddle(string) {
  const middleIndex = string.length / 2;
  if (string.length % 2 == 0)
    return `${string.charAt(middleIndex - 1)}${string.charAt(middleIndex)}`;
  return string.charAt(middleIndex);
}

console.log(getMiddle("test"));
