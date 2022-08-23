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

    private static string Solve(int n)
    {
        int c2 = n / 3;
        int c1 = c2 * 3 == n ? c2 : c2 + 1;
        if (c1 * 1 + c2 * 2 != n)
        {
            int temp = c1;
            c1 = c2;
            c2 = temp;
        }
        return string.Format("{0} {1}", c1, c2);
    }
}