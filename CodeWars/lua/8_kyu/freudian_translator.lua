-- https://www.codewars.com/kata/5713bc89c82eff33c60009f7/train/lua

function toFreud(sentence)
    local output = ""
    local whitespace_count = 0

    for i = 1, #sentence do
        if string.sub(sentence, i, i) == " " then
            whitespace_count = whitespace_count + 1
        end
    end

    local word_count = whitespace_count + 1
    for i = 1, word_count do
        if i ~= word_count then
            output = output .. "sex "
        else
            output = output .. "sex"
        end
    end
    
    return output
end
  
return toFreud