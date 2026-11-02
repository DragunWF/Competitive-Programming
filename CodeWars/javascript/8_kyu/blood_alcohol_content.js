// https://www.codewars.com/kata/571b6a4a7beb0a8ade0007a8

function bloodAlcoholContent(drinks, weight, sex, time) {
  const alcoholDistributionRatio = sex === "male" ? 0.73 : 0.66;
  const totalAlcohol = drinks.ounces * drinks.abv;
  const result =
    ((totalAlcohol * 5.14) / weight) * alcoholDistributionRatio - 0.015 * time;
  return Number(result.toFixed(4));
}
