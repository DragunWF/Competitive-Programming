// https://www.codewars.com/kata/526dbd6c8c0eb53254000110

function alphanumeric(string) {
  const x = [" ", "_", "!", "&", "(", ")", "$", " "];
  for (c of string) if (x.includes(c)) return false;
  return string.length > 0 ? true : false;
}
