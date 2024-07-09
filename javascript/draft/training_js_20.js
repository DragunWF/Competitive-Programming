// https://www.codewars.com/kata/57284d23e81185ae6200162a/train/javascript

function topSecret(str) {
  const alphabets = "abcdefghijklmnopqrstuvwxyz";
  let output = "";
  for (let i = 0; i < str.length; i++) {
    if (str.charAt(i) === " ") {
      output += " ";
      continue;
    }
    const code = str.charCodeAt(i);
    console.log(code);
    if (code >= 65 && code <= 90) {
      output += alphabets.charAt(65 - code).toUpperCase();
    }
    if (code >= 97 && code <= 122) {
      output += alphabets.charAt(97 - code);
    }
  }
  return output;
}

//question1: The top secret file number is...
answer1 = "?";
//question2: Super agent's name is...
answer2 = "?";
//question3: He stole the treasure is...
answer3 = "?";

function test() {
  // Not part of the solution
  console.log(topSecret("Pb qdph lv Mrkq"));
}

test();
