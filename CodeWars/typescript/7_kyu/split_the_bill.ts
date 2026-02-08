// https://www.codewars.com/kata/5641275f07335295f10000d0/typescript

export function splitTheBill(x: { [k: string]: number }): {
  [k: string]: number;
} {
  let totalSpent: number = 0;
  for (let key of Object.keys(x)) {
    totalSpent += x[key];
  }

  let targetBillSplit = totalSpent / Object.keys(x).length;
  const output: { [k: string]: number } = {};
  for (let key of Object.keys(x)) {
    output[key] = Number((x[key] - targetBillSplit).toFixed(2));
  }
  return output;
}
