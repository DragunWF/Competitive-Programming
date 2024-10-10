// https://www.codewars.com/kata/514a024011ea4fb54200004b

function domainName(url) {
  if (url.includes("http")) {
    let arr = url.split("/");
    let n = arr[2].includes("www.") ? 1 : 0;
    return arr[2].split(".")[n];
  }
  return url.split(".")[url.split(".").length > 2 ? 1 : 0];
}
