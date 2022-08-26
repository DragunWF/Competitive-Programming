using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string s = Console.ReadLine();
        Console.WriteLine(Solve(n, s));
    }

    private static int Solve(int n, string s)
    {
        int removals = 0;
        int chainedXs = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == 'x')
            {
                chainedXs++;
                if (chainedXs >= 3)
                    removals++;
            }
            else
                chainedXs = 0;
        }
        return removals;
    }
}