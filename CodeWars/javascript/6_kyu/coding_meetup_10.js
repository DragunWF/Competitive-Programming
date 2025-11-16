// https://www.codewars.com/kata/coding-meetup-number-10-higher-order-functions-series-create-usernames

function addUsername(list) {
  const output = [];
  for (let user of list) {
    let username = user.firstName.toLowerCase();
    username += user.lastName[0].toLowerCase();
    const currentYear = parseInt(new Date().toString().split(" ")[3]);
    username += currentYear - user.age;
    user.username = username;
    output.push(user);
  }
  return output;
}

function test() {
  console.log(
    addUsername([
      {
        firstName: "Emily",
        lastName: "N.",
        country: "Ireland",
        continent: "Europe",
        age: 30,
        language: "Ruby",
      },
      {
        firstName: "Nor",
        lastName: "E.",
        country: "Malaysia",
        continent: "Asia",
        age: 20,
        language: "Clojure",
      },
    ])
  );
}

test();
