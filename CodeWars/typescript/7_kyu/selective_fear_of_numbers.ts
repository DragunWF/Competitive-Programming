// https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/typescript

export function amIAfraid(day: string, num: number): boolean {
  if (day === "Monday" && num === 12) return true;
  if (day === "Tuesday" && num > 95) return true;
  if (day === "Wednesday" && num === 34) return true;
  if (day === "Thursday" && num === 0) return true;
  if (day === "Friday" && num % 2 === 0) return true;
  if (day === "Saturday" && num === 56) return true;
  if (day === "Sunday" && (num === 666 || num === -666)) return true;
  return false;
}
