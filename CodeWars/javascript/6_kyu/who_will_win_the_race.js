// https://www.codewars.com/kata/62bdf18465dff9005e5367d4/train/javascript

function whoWillWin(arr) {
  if (!arr.length) return "No one raced!";

  let fastestRacers = [];
  let fastestTime = Infinity;
  for (let racer of arr) {
    const parsedSpeed = parseFloat(racer.speed.split(" ")[0]);
    if (parsedSpeed <= 0) continue;
    const parsedDistance = parseFloat(racer.distanceToRun.split(" ")[0]);
    if (parsedDistance <= 0) continue;

    const timeTaken = parsedDistance / parsedSpeed;
    if (timeTaken > 0 && timeTaken < fastestTime) {
      fastestRacers = [racer.name];
      fastestTime = timeTaken;
    } else if (timeTaken === fastestTime) {
      fastestRacers.push(racer.name);
    }
  }

  fastestTime = Math.round(fastestTime);
  if (fastestRacers.length > 1) {
    return `${fastestRacers.length} people tied in ${fastestTime} second(s)!`;
  } else if (!fastestRacers.length) {
    return "Everyone was disqualified!";
  }
  return `${fastestRacers[0]} won the race in ${fastestTime} second(s)!`;
}

function test() {
  // Alex won the race in 33 second(s)!
  console.log(
    whoWillWin([
      {
        name: "Alex",
        speed: "3 meter(s) per second",
        distanceToRun: "100 meter(s)",
      },
      {
        name: "Sophia",
        speed: "6 meter(s) per second",
        distanceToRun: "300 meter(s)",
      },
      {
        name: "Timmy",
        speed: "4 meter(s) per second",
        distanceToRun: "200 meter(s)",
      },
      {
        name: "Ben",
        speed: "2 meter(s) per second",
        distanceToRun: "68 meter(s)",
      },
    ]),
  );

  // A Turtle won the race in 10000 second(s)!
  console.log(
    whoWillWin([
      {
        name: "A Turtle",
        speed: "0.1 meter(s) per second",
        distanceToRun: "1000 meter(s)",
      },
    ]),
  );
}

test();
