// https://www.codewars.com/kata/580e67ae22e42d797000015e/train/javascript

function isItBugged(code) {
  const values = code.split(" ");
  if (values.length !== 2) return false;
  const isValidDate = validateDate(values[0]);
  const isValidTime = validateTime(values[1]);
  return isValidDate && isValidTime;
}

function validateTime(time) {
  const values = time.split(":");
  if (values.length !== 2) return false;
  let hours = values[0];
  let minutes = values[1];
  if (hours.length !== 2 || minutes.length !== 2) return false;
  try {
    hours = parseInt(hours);
    minutes = parseInt(minutes);
    if (hours >= 24 || hours < 0 || minutes >= 60 || minutes < 0) return false;
  } catch (err) {
    return false;
  } finally {
    return true;
  }
}

function validateDate(date) {
  const values = date.split("-");
  if (values.length !== 3) return false;
  let day = values[0];
  let month = values[1];
  let year = values[2];
  if (day.length !== 2 || month.length !== 2 || year.length !== 4) return false;
  try {
    day = parseInt(day);
    month = parseInt(month);
    year = parseInt(year);
  } catch (err) {
    return false;
  } finally {
    return true;
  }
}

function test() {
  // Test cases
  console.log(isItBugged("14-10-2016 01:12")); // true
}

test();
