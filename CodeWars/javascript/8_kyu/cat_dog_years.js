// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/javascript

const toAnimalYears = (humanYears, type) => {
  let result = humanYears ? 15 : 0;
  let incrementor = type === "cat" ? 4 : 5;
  if (humanYears >= 2) result += 9;
  if (humanYears > 2) result += incrementor * (humanYears - 2);
  return result;
};

const humanYearsCatYearsDogYears = (humanYears) => {
  const catYears = toAnimalYears(humanYears, "cat");
  const dogYears = toAnimalYears(humanYears, "dog");
  return [humanYears, catYears, dogYears];
};
