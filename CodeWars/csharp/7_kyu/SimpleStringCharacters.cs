// https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/csharp

using System;

public class Solution
{
    public static int[] solve(String s)
    {
        int uppercase = 0, lowercase = 0, numbers = 0, special = 0;
        foreach (char c in s)
        {
            if (char.IsDigit(c))
            {
                numbers++;
            }
            else if (char.IsLetter(c))
            {
                string strChar = c.ToString();
                if (strChar == strChar.ToUpper())
                {
                    uppercase++;
                }
                else
                {
                    lowercase++;
                }
            }
            else
            {
                special++;
            }
        }
        return new int[] { uppercase, lowercase, numbers, special };
    }
}