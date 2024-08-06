// https://www.codewars.com/kata/54e8c3e89e2ae6f4900005a1/train/javascript

var questions = [
  {
    question: "What's the currency of the USA?",
    choices: ["US dollar", "Ruble", "Horses", "Gold"],
    corAnswer: 0,
  },
  {
    question: "Where was the American Declaration of Independence signed?",
    choices: ["Philadelphia", "At the bottom", "Frankie's Pub", "China"],
    corAnswer: 0,
  },
];

function addProperty(questions) {
  output = [];
  for (let i = 0; i < questions.length; i++) {
    questions[i]["usersAnswer"] = null;
    output.push(questions[i]);
  }
  return output;
}

console.log(addProperty(questions));
