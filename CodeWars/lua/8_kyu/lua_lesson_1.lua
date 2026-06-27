-- https://www.codewars.com/kata/59fee4e680171f01f200008a/train/lua

kata = {}
function kata.firstLua(a,b,c)
  return string.format("%s %s %s", a, a * b, b >= c and "Lua" or "Codewars")
end

return kata