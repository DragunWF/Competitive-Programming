// https://www.codewars.com/kata/5758a91bbd1fdd2033000947/train/javascript

function anArgument(...args) {
  const values = args;
  if (!values.length) {
    return "You didn't give me any arguments.";
  }
  for (let i = 0; i < values.length; i++) {
    values[i] = `"${values[i]}"`;
  }

  let output = `You gave me ${values.length} ${
    values.length === 1 ? "argument" : "arguments"
  } and `;
  if (values.length === 1) {
    output += `it is ${values[0]}.`;
  } else if (values.length === 2) {
    output += `they are ${values[0]} and ${values[1]}.`;
  } else {
    const items = values.slice(0, values.length - 1);
    output += `they are ${items.join(", ")} and ${values[values.length - 1]}.`;
  }
  return output;
}

function test() {
  console.log(anArgument("pigs", "giraffes", "unicorns"));
}

test();

// 'You gave me 4 arguments and they are "chairs", "table", "lamp", and "sideboard".'

// 'You gave me 4 arguments and they are "chairs", "table", "lamp" and "sideboard".'
