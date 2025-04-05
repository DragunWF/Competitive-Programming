-- https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/lua

local function list_animals(animals)
    local str = "";
    
    for i = 1, #animals do
      str = str .. i .. ". " .. animals[i] .. "\n";
    end
    
    return str;
end
  
return list_animals;