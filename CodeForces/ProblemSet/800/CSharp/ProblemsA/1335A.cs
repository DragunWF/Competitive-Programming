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
        if (n <= 2)
            return 0;
        return n / 2 - (n % 2 == 0 ? 1 : 0);
    }
}