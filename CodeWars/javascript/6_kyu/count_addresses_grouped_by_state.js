// https://www.codewars.com/kata/55f8370b0229d3dad000007a/train/javascript

function count(addresses) {
  const counters = {};
  for (let address of addresses) {
    if (!address.state) {
      throw new Error("No state in address!");
    }
    if (address.state in counters) {
      counters[address.state]++;
    } else {
      counters[address.state] = 1;
    }
  }
  return mapStates(counters);
}

function mapStates(counters) {
  const output = [];
  for (let state of Object.keys(counters)) {
    output.push({
      state,
      count: counters[state],
    });
  }
  return output;
}
