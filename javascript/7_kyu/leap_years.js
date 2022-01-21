// https://www.codewars.com/kata/526c7363236867513f0005ca

function isLeapYear(year) {
  if (!(year % 4)) {
    if (!(year % 400)) return true;
    if (!(year % 100)) return false;
    return true;
  }
  return false;
}
