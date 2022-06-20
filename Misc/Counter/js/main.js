$(document).ready(() => {
  const incrementButton = $("#increment");
  const decrementButton = $("#decrement");

  const problemsSolvedElement = $("#problemsSolved");
  let problemsSolvedValue = 0;

  function updateProblemsSolvedText() {
    problemsSolvedElement.text(problemsSolvedValue.toString());
  }

  incrementButton.click(() => {
    problemsSolvedValue++;
    updateProblemsSolvedText();
  });

  decrementButton.click(() => {
    problemsSolvedValue--;
    if (problemsSolvedValue < 0) problemsSolvedValue = 0;
    updateProblemsSolvedText();
  });
});
