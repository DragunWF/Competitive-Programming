// https://www.codewars.com/kata/57ed6361e77282ee9300019f/train/javascript

function fifa(ticket, results) {
  let winnings = 0;
  for (let i = 0; i < results.length; i++) {
    const result = results[i];
    const values = result.split("-");
    const home = parseInt(values[0]);
    const away = parseInt(values[1]);
    if (i == 0 && home > away) winnings += convertToInt(ticket.Home);
    else if (i == 1 && home < away) winnings += convertToInt(ticket.Away);
    else if (i == 2 && home === away) winnings += convertToInt(ticket.Draw);
  }
  return `£${winnings}`;
}

function convertToInt(currency) {
  return parseInt(currency.substring(1));
}

function test() {
  // '£5075'
  console.log(
    fifa({ Home: "£75", Away: "£5000", Draw: "£1324" }, ["1-0", "2-3", "0-1"])
  );
}

test();
