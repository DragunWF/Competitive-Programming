// https://www.codewars.com/kata/57642a90dee2da8dd3000161/train/typescript

export function arr2bin(arr: any[]): string {
  let sum = 0;
  for (let item of arr) {
    if (typeof item === "number") {
      sum += item;
    }
  }
  return sum.toString(2);
}
