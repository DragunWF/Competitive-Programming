// https://www.codewars.com/kata/5a3dd29055519e23ec000074

function checkExam(array1, array2) {
  let score = 0;
  for (let i = 0; i < array1.length; i++) {
    if (!array2[i].length) continue;
    else if (array1[i] === array2[i]) score += 4;
    else score -= 1;
  }
  return score < 0 ? 0 : score;
}
