// https://www.codewars.com/kata/525caa5c1bf619d28c000335

function isSolved(board) {
  board = [...board[0], ...board[1], ...board[2]];
  if (!board.includes(0)) return 0;
  const conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 4, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let p = 1; p < 3; p++) {
    for (c of conditions) {
      if (board[c[0]] === p && board[c[1]] === p && board[c[2]] === p) return p;
    }
  }
  return -1;
}
