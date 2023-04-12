// https://www.codewars.com/kata/5842df8ccbd22792a4000245

function expandedForm(num) {
  let output = [];
  const strNum = num.toString();
  for (let i = 0; i < strNum.length; i++) {
    if (strNum.charAt(i) !== "0") {
      const nth = Number(`1${"0".repeat(strNum.length - i - 1)}`);
      output.push(Number(strNum.charAt(i)) * nth);
    }
  }
  return output.join(" + ");
}

// Not part of the solution
function test() {
  const testCases = [12, 42, 70304, 12345, 500000];
  for (let i = 0; i < testCases.length; i++) {
    const result = expandedForm(testCases[i]);
    console.log(`Test Case #${i + 1}: ${result}`);
  }
}

test();
