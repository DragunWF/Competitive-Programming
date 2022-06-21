function solve(n, s) {
  var a = 0;
  var d = 0;
  for (var i = 0; i < n; i++) {
    if (s[i] === "A") a++;
    else d++;
  }
  if (a === d) return "FRIENDSHIP";
  return a > d ? "Anton" : "Danik";
}

function main() {
  var n = Number(readline());
  var s = readline();
  console.log(solve(n, s));
}

main();
