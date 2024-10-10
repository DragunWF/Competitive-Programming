// https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

function replace(s) {
  const vowels = "aeiouAEIOU".split("");
  return s
    .split("")
    .map((n) => {
      return vowels.includes(n) ? "!" : n;
    })
    .join("");
}
