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
            int k = v[2];
            Console.WriteLine(Solve(a, b, k));
        }
    }

    private static long Solve(int a, int b, int k)
    {
        bool m = k % 2 == 0;
        long x = (k + (m ? 0 : 1)) / 2;
        long y = m ? x : x - 1;
        return a * x - b * y;
    }
}