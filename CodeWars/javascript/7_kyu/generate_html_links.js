// https://www.codewars.com/kata/56896f078dcf3e886c000067/train/javascript

function generateMenu(menuItems) {
  if (!menuItems.length) return "";
  const tags = [];
  for (let properties of menuItems) {
    tags.push(`<a href="${properties.url}">${properties.text}</a>`);
  }
  return tags.join("");
}
