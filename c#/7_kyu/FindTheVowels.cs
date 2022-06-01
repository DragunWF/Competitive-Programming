using System;
using System.Linq;
using System.Collections.Generic;

public class Kata
{
    public static int[] VowelIndices(string word)
    {
        var vowels = new char[6] { 'a', 'e', 'i', 'o', 'u', 'y' };
        var indexes = new List<int>();
        for (var i = 0; i < word.Length; i++)
            if (vowels.Contains(char.ToLower(word[i])))
                indexes.Add(i + 1);
        return indexes.ToArray();
    }
}

// https://www.codewars.com/kata/5680781b6b7c2be860000036/train/csharp