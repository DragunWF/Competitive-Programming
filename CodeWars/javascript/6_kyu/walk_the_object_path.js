// https://www.codewars.com/kata/59418db3f5c394eca80000ef/train/javascript

function find(object, path) {
  const keys = path.split(".");
  const digits = "0123456789";
  let currentValue = null;
  try {
    for (let key of keys) {
      if (digits.includes(key)) {
        currentValue = currentValue[parseInt(key)];
      } else {
        currentValue = currentValue === null ? object[key] : currentValue[key];
        if (typeof currentValue === "function") return undefined;
      }
    }
    return currentValue;
  } catch (err) {
    return undefined;
  }
}
