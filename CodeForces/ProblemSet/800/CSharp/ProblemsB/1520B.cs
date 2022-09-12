using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(Solve(n));
        }
    }

    private static int Solve(int n)
    {
        if (n <= 9)
            return n;

        string s = n.ToString();
        int digitCount = s.Length;
        int lastDigit = int.Parse(s[0].ToString());

        string nextOrdinary = "";
        for (int i = 0; i < digitCount; i++)
            nextOrdinary += lastDigit.ToString();

        int extraOrdinaryNums = lastDigit - 1;
        if (n >= int.Parse(nextOrdinary))
            extraOrdinaryNums++;

        return (digitCount - 1) * 9 + extraOrdinaryNums;
    }
}