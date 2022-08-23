using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int x = int.Parse(Console.ReadLine());
            Console.WriteLine(Solve(x));
        }
    }

    private static int Solve(int x)
    {
        int digitCount = x.ToString().Length;
        int n = int.Parse(x.ToString()[0].ToString());

        int p = (n - 1) * 10;
        for (int i = 1; i <= digitCount; i++)
            p += i;

        return p;
    }
}