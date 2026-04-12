// https://www.codewars.com/kata/5817c0148e74302c4800039c/train/javascript

const bot = {
  message(prompt) {
    const words = prompt.split(" ");
    if (words[0] === "Add" || words[0] === "Subtract") {
      const isAddition = words[0] === "Add";
      if (isAddition) {
        return parseInt(words[1]) + parseInt(words[3]);
      }
      return parseInt(words[3]) - parseInt(words[1]);
    }
    if (words[0] === "What") {
      const lastWord = words[words.length - 1];
      const meridiem = lastWord.slice(-3).substring(0, 2);

      const timeValues = lastWord.split(":");
      let hour = parseInt(timeValues[0]);
      let minutes = parseInt(timeValues[1]);

      if (hour === 12) {
        hour = 0;
      }
      if (
        (hour >= 6 && meridiem === "am") ||
        ((hour < 6 || (hour === 6 && minutes === 0)) && meridiem === "pm")
      ) {
        return "sunny";
      }
      return "raining";
    }
    return "?";
  },
};
