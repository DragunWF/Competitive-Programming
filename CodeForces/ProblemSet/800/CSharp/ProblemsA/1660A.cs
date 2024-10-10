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
            int[] v = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int a = v[0];
            int b = v[1];
            Console.WriteLine(Solve(a, b));
        }
    }

    private static int Solve(int a, int b)
    {
        return a == 0 ? 1 : a + b * 2 + 1;
    }
}