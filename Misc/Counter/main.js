$(document).ready(() => {
  const incrementButton = $("#increment");
  const decrementButton = $("#decrement");

  const problemsSolvedElement = $("#problemSolved");
  const problemsSolvedValue = 0;

  function updateProblemsSolvedText() {
    problemsSolvedElement.text(problemsSolvedValue.toString());
  }

  incrementButton.onClick(() => {
    problemsSolvedValue++;
    updateProblemsSolvedText();
  });

  decrementButton.onClick(() => {
    problemsSolvedValue--;
    updateProblemsSolvedText();
  });
});
