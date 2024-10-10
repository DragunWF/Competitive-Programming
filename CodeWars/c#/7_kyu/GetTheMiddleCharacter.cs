// https://www.codewars.com/kata/56747fd5cb988479af000028/train/csharp

using System;

public class Kata
{
    public static string GetMiddle(string s)
    {
        var length = s.Length;
        var middle = length / 2;
        if (length % 2 == 0)
            return String.Format("{0}{1}", s[middle - 1], s[middle]);
        return s[middle].ToString();
    }
}
