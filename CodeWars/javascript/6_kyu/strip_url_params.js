// https://www.codewars.com/kata/51646de80fd67f442c000013/train/javascript

function stripUrlParams(url, paramsToStrip = []) {
  if (url.indexOf("?") === -1) return url;
  const urlParts = url.split("?");
  const parameters = urlParts[1].split("&");
  const currentParameters = [];
  const uniqueNames = [];
  for (let parameter of parameters) {
    const name = parameter.split("=")[0];
    if (!paramsToStrip.includes(name) && !uniqueNames.includes(name)) {
      currentParameters.push(parameter);
      uniqueNames.push(name);
    }
  }
  return `${urlParts[0]}${
    currentParameters.length > 0 ? "?" : ""
  }${currentParameters.join("&")}`;
}

function test() {
  // Not part of the solution, just testing
  console.log(stripUrlParams("www.codewars.com?a=1&b=2&a=1&b=3", ["b"]));
  console.log(stripUrlParams("www.codewars.com", ["b"]));
}

test();
