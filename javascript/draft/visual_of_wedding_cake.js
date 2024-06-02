// https://www.codewars.com/kata/662f64adf925ebceb6c5a4e4

function cakeVisualizer(s) {
  const layers = s.split("\n");
  const output = [];
  for (let layer of layers) {
    let modified = "";
    for (let i = 0; i < layer.length; i++) {
      if (i === 0 || i === layer.length - 1) {
        modified += layer[i];
      } else {
        modified += " ";
      }
    }
    modified[modified.length / 2] = "|";
    output.push(modified);
  }
  return output.join("\n");
}

// Not part of the solution
function test() {
  const str = "/|\\\n\\/ \\/\n\\ | | \\\n/\\/\\/\\/\n/       \\\n/|||||||||\\";
  console.log(cakeVisualizer(str));
}

test();
