// https://www.codewars.com/kata/525f0459fb9570f9ff00005d/train/javascript

function searchNames(logins) {
  const output = [];
  let isEmail = false;
  let isTargetUser = false;
  for (let i = 0; i < logins.length; i++) {
    const item = logins[i];
    if (isEmail && isTargetUser) {
      output.push(item);
      isTargetUser = false;
    } else {
      isTargetUser = item.startsWith(".") || item.endsWith(".");
    }
    isEmail = !isEmail;
  }
  return output;
}

function test() {
  // Expected: [ "food@bar.com" ]
  console.log(
    searchNames([
      "foo",
      "foo@bar.com",
      "bar",
      "bar@foo.com",
      ".foo",
      "food@bar.com",
    ])
  );
}

test();
