// https://www.codewars.com/kata/54e6533c92449cc251001667/train/javascript

const uniqueInOrder = (iterable) => {
  const uniques = iterable.length ? [iterable[0]] : [];
  for (let i = 1; i < iterable.length; i++)
    if (iterable[i] !== iterable[i - 1]) 
      uniques.push(iterable[i]);
  return uniques;
};
