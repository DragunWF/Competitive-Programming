// https://www.codewars.com/kata/53b2f6934a240823f4000abc/train/javascript

function uniquePush(arr, obj) {
  if (!obj.phoneNumber) return false;
  for (let person of arr)
    if (person.phoneNumber === obj.phoneNumber) return false;
  arr.push(obj);
  return true;
}
