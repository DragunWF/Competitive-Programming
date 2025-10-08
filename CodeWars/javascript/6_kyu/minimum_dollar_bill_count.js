// https://www.codewars.com/kata/58e4d3530e1018e155000058/train/javascript

function minimumBillCount(value, availables) {
  let billCount = 0;
  let currentValue = value;
  while (currentValue != 0) {
    const selectedBill = getMaxBill(currentValue, availables);
    const dividedBills = Math.floor(currentValue / selectedBill);
    billCount += dividedBills;
    currentValue -= dividedBills * selectedBill;
  }
  return billCount;
}

function getMaxBill(currentValue, availables) {
  let maxBill = 0;
  for (let available of availables) {
    if (available <= currentValue && available > maxBill) {
      maxBill = available;
    }
  }
  return maxBill;
}

function test() {
  console.log(minimumBillCount(100, [10, 50, 20])); // 2
}

test();
