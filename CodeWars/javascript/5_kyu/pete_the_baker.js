// https://www.codewars.com/kata/525c65e51bf619685c000059/train/javascript

function cakes(recipe, available) {
  const canMake = [];
  for (let incredient in recipe) {
    if (available[incredient] == undefined) return 0;
    const quantity = Math.floor(available[incredient] / recipe[incredient]);
    if (quantity >= 0) canMake.push(quantity);
  }
  return getMin(canMake);
}

function getMin(arr) {
  let minNum = arr[0];
  for (let i = 1; i < arr.length; i++) 
    if (arr[i] < minNum) minNum = arr[i];
  return minNum;
}

console.log(
  cakes(
    { flour: 500, sugar: 200, eggs: 1 },
    { flour: 1200, sugar: 1200, eggs: 5, milk: 200 }
  )
); // must return 2

console.log(
  cakes(
    { apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100 },
    { sugar: 500, flour: 2000, milk: 2000 }
  )
); // must return 0
