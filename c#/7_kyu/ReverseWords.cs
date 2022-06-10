using System;
using System.Collections.Generic;

public static class Kata
{
    public static string ReverseWords(string str)
    {
        var output = new List<string>();
        foreach (var word in str.Split(' '))
        {
            var reversedWord = word.ToCharArray();
            Array.Reverse(reversedWord);
            output.Add(string.Join("", reversedWord));
        }
        return string.Join(" ", output);
    }
}