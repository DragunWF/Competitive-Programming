// https://www.codewars.com/kata/coding-meetup-number-16-higher-order-functions-series-ask-for-missing-details

function askForMissingDetails(users) {
  let questionedUsers = [];
  for (let user of users) {
    for (let key in user) {
      if (user[key] === null) {
        user.question = `Hi, could you please provide your ${key}.`;
        questionedUsers.push(user);
        break;
      }
    }
  }
  return questionedUsers;
}

function test() {
  console.log(
    askForMissingDetails([
      {
        firstName: null,
        lastName: "I.",
        country: "Argentina",
        continent: "Americas",
        age: 35,
        language: "Java",
      },
      {
        firstName: "Lukas",
        lastName: "X.",
        country: "Croatia",
        continent: "Europe",
        age: 35,
        language: null,
      },
      {
        firstName: "Madison",
        lastName: "U.",
        country: "United States",
        continent: "Americas",
        age: 32,
        language: "Ruby",
      },
    ])
  );
}

test();
