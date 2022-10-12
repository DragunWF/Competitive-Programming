let numberToMoney = (n) => {
  const nStr = n.toString().split(".");
  const firstHalf = nStr[0].split("");
  firstHalf.reverse();

  let withComma = "";
  for (let i = 0; i < firstHalf.length; i++) {
    withComma += firstHalf[i];
    if ((i + 1) % 3 === 0 && i + 1 < firstHalf.length) withComma += ",";
  }

  withComma = withComma.split("");
  withComma.reverse();
  let secondHalf = nStr[1].substring(0, 2);
  if (secondHalf[0] !== "0" && secondHalf[1] === "0")
    secondHalf = secondHalf[0];

  return `${withComma.join("")}${secondHalf !== "00" ? `.${secondHalf}` : ""}`;
};

console.log(numberToMoney(2546.2562));
