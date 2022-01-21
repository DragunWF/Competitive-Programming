// https://www.codewars.com/kata/53368a47e38700bd8300030d

function list(names) {
  let output = "";
  let len = names.length;
  for (x of names) {
    let index = names.indexOf(x);
    if (len > 2) {
      if (index === len - 1) output += `${x.name}`;
      else if (index !== len - 2) output += `${x.name}, `;
      else output += `${x.name} & `;
    } else {
      if (index !== len - 1) output += `${x.name} & `;
      else output += `${x.name}`;
    }
  }
  return output;
}
