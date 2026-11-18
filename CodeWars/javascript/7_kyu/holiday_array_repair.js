// https://www.codewars.com/kata/5579906f2f0c0d0766000127/train/javascript

function holidayCount(a1, a2) {
  let a1TotalDays = totalHolidays(a1);
  let a2TotalDays = totalHolidays(a2);
  if (a1TotalDays === null || a2TotalDays === null) {
    return "Not possible";
  }
  if (a1TotalDays === a2TotalDays) {
    return "Same";
  }
  return a1TotalDays > a2TotalDays ? "Right" : "Wrong";
}

function totalHolidays(arr) {
  let totalDays = null;
  for (let item of arr) {
    if (typeof item === "number" && item % 1 === 0) {
      if (totalDays === null) {
        totalDays = 0;
      }
      totalDays += item;
    }
  }
  return totalDays;
}
