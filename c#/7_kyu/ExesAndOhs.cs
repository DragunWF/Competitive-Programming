// https://www.codewars.com/kata/55908aad6620c066bc00002a/train/csharp

using System.Linq;
using System;

public static class Kata 
{
  public static bool XO (string input)
  {
    string str = input.ToLower();
    int xCount = 0, oCount = 0;
    for (int i = 0; i < str.Length; i++) 
    {
      if (str[i] == 'x') xCount++;
      else if (str[i] == 'o') oCount++;
    }
    return xCount == oCount;
  }
}