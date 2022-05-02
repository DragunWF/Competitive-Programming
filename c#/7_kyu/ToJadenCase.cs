using System;
using System.Collections.Generic;

public static class JadenCase
{
  public static string ToJadenCase(this string phrase)
  {
    var words = phrase.Split(" ");
    var output = new List<string>();
    foreach (var word in words) 
      output.Add(char.ToUpper(word[0]) + word.Substring(1, word.Length - 1));
    return string.Join(" ", output);
  }
}

// https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/csharp