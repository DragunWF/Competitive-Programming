// https://www.codewars.com/kata/64de4832c734e7036b455536/train/javascript

function getTask(ocean) {
  let submarineDepth = null;
  let submarineLength = 0;
  let isSubmarineDestroyed = false;
  for (let i = 0; i < ocean.length; i++) {
    const submarine = getSubmarine(ocean[i]);
    if (submarine.isValid) {
      submarineDepth = i;
      submarineLength = submarine.size;
      isSubmarineDestroyed = submarine.isDestroyed;
      break;
    }
  }
  if (isSubmarineDestroyed) return "Emergency assistance to victims";
  if (submarineDepth === 0) return "Look for a submarine on the surface";
  if (submarineLength < submarineDepth)
    return `Emergency search for a possibly damaged submarine at ${submarineDepth} depth`;
  return `Start searching for a submarine at ${submarineDepth} depth`;
}

function getSubmarine(row) {
  const submarine = {
    isValid: false,
    size: 1,
    isDestroyed: false,
  };
  const submarineParts = ["(", "O", ")"];
  for (let i = 0; i < row.length; i++) {
    if (submarineParts.includes(row[i])) {
      submarine.isValid = true;
      break;
    }
  }
  if (!submarine.isValid) return submarine;

  const start = row.indexOf("(");
  for (let i = start + 1; i < row.length; i++) {
    const element = row[i];
    if (element === ")" || element === "O") {
      submarine.size++;
      if (element === ")") break;
    } else {
      submarine.isDestroyed = true;
      break;
    }
  }

  return submarine;
}

function test() {
  console.log(
    getTask([
      ["~", "~", "~", "~", "~"],
      ["ˑ", "ˑ", "ˑ", "ˑ", "ˑ"],
      ["ˑ", "(", "O", ")", "ˑ"], // <- A submarine size 3 at a depth of 2
      ["ˑ", "ˑ", "ˑ", "ˑ", "ˑ"],
      ["ˑ", "ˑ", "ˑ", "ˑ", "ˑ"],
    ])
  );
  console.log(
    getTask(
      [
        ["~", "~", "~", "~", "~"],
        ["ˑ", "(", "O", ")", "ˑ"],
        ["ˑ", "ˑ", "ˑ", "ˑ", "ˑ"],
      ] // Response - 'Start searching for a submarine at 1 depth'
    )
  );
}

test();
