// https://www.codewars.com/kata/55327e12f5363713200000e4

var regex = undefined;

function isJojo(name) {
  name = name.toLowerCase().split(" ");
  if (name[0].startsWith("jo"))
    if (name[1].startsWith("jo") || name[1].endsWith("jo")) return true;
  if (name[0].startsWith("gio") && name[1].startsWith("gio")) return true;
  return false;
}
