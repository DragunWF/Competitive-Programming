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
            int x = v[0];
            int y = v[1];
            int a = v[2];
            int b = v[3];
            Console.WriteLine(Solve(x, y, a, b));
        }
    }

    private static int Solve(int x, int y, int a, int b)
    {
        int d = Math.Abs(x - y);
        int r = a + b;
        return d % r == 0 ? d / r : -1;
    }
}