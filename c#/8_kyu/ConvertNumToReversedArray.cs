// https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/csharp

using System;
using System.Collections.Generic;

namespace Solution
{
  class Digitizer
  {
    public static long[] Digitize(long n)
    {
      string str = n.ToString();
      long[] output = new long[str.Length];
      for (int i = str.Length - 1; i >= 0; i--) 
      {
        output[str.Length - (i + 1)] = long.Parse(str[i].ToString());
      }
      return output;
    }
  }
}