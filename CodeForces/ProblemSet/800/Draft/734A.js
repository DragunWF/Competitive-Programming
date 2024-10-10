function solve(n, s) {
  let a = 0;
  let d = 0;
  for (let i = 0; i < n; i++) {
    if (s[i] === "A") a++;
    else d++;
  }
  if (a === d) return "FRIENDSHIP";
  return a > d ? "Anton" : "Danik";
}

function main() {
  const n = Number(readline());
  const s = readline();
  console.log(solve(n, s));
}

main();
