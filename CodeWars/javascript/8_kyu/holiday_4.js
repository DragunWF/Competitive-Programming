// https://www.codewars.com/kata/57e921d8b36340f1fd000059/train/javascript

function shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin) {
  if (dolphin) {
    sharkSpeed /= 2;
  }
  let currentPontoonDistance = pontoonDistance;
  let currentSharkDistance = sharkDistance;
  while (currentPontoonDistance > 0 && currentSharkDistance > 0) {
    currentPontoonDistance -= youSpeed;
    currentSharkDistance -= sharkSpeed;
  }
  if (currentSharkDistance <= 0) return "Shark Bait!";
  return "Alive!";
}
