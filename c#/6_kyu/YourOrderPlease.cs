using System;
using System.Collections;
using System.Collections.Generic;

public static class Kata
{
    public static string Order(string words)
    {
        if (string.IsNullOrEmpty(words))
            return "";

        var sentence = words.Split(" ");
        var ordered = new List<string>();
        var start = 0;
        while (sentence.Length > ordered.Count)
        {
            foreach (var word in sentence)
            {
                var characters = word.ToCharArray();
                Array.Sort(characters);
                if (Convert.ToByte(characters[0].ToString()) == start + 1)
                {
                    ordered.Add(word);
                    start++;
                }
            }
        }
        return string.Join(" ", ordered);
    }
}
