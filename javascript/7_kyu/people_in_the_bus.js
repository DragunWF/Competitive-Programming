// https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/javascript

let number = (busStops) => {
  let peopleInBus = 0;
  for (let stop of busStops) {
    peopleInBus += stop[0];
    peopleInBus -= stop[1];
  }
  return peopleInBus;
};
