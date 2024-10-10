// https://www.codewars.com/kata/63d1bac72de941033dbf87ae

function validateSudoku(board) {
  const blocks = [];
  const singularBlock = [];
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      const nth = j + 1;
      singularBlock.push(board[i][j]);
      if (j % 3 === 0) {
        blocks.push(singularBlock);
        singularBlock = [];
      }
    }
  }
  return validateAllBlocks(blocks);
}

function validateAllBlocks(blocks) {
  for (let block of blocks) {
    if (!validateBlock(block)) {
      return false;
    }
  }
  return true;
}

function validateBlock(block) {
  // add validation logic
  return;
}

// Not part of the solution
function test() {
  const testCases = [{ content: null, expected: false }];
  for (let i = 0; i < testCases.length; i++) {
    const answer = validateSudoku(testCases[i].expected);
    console.log(`Test Case #${i + 1}: ${answer}`);
    if (testCases[i].expected !== answer) {
      console.log(
        `Failed Test CaseGot ${answer}, expected ${testCases[i].expected}`
      );
    }
  }
}

test();
