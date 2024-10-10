using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] p = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        Console.WriteLine(Solve(n, p));
    }

    private static string Solve(int n, int[] p)
    {
        int[] r = new int[n];
        for (int i = 0; i < n; i++)
            r[p[i] - 1] = i + 1;
        return string.Join(' ', r);
    }
}