// https://www.codewars.com/kata/57b56af6b69bfcffb80000d7/train/javascript

function toInitials(name) {
  const output = [];
  const nameParts = name.split(" ");
  for (let part of nameParts) {
    output.push(part.charAt(0).toUpperCase() + ".");
  }
  return output.join(" ");
}
