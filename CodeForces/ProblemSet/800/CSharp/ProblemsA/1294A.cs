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
            int[] v = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            int[] s = { v[0], v[1], v[2] };
            int n = v[3];
            Console.WriteLine(Solve(s, n));
        }
    }

    private static string Solve(int[] s, int n)
    {
        Array.Sort(s);
        for (int i = 0; i < 2; i++)
            n -= s[2] - s[i];
        return n >= 0 && n % 3 == 0 ? "YES" : "NO";
    }
}