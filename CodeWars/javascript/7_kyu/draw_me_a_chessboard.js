// https://www.codewars.com/kata/56242b89689c35449b000059/train/javascript

function chessBoard(rows, columns) {
  let rowCog = true;
  const chessBoard = [];
  for (let i = 0; i < rows; i++) {
    const row = [];
    let columnCog = true;
    for (let j = 0, n = 1; j < columns; j++, n++) {
      if (columnCog) {
        row.push(rowCog ? "O" : "X");
      } else {
        row.push(rowCog ? "X" : "O");
      }
      columnCog = !columnCog;
    }
    chessBoard.push(row);
    rowCog = !rowCog;
  }
  return chessBoard;
}
