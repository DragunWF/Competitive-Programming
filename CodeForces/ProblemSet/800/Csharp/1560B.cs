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
            int c = v[2];
            Console.WriteLine(Solve(a, b, c));
        }
    }

    private static int Solve(int a, int b, int c)
    {
        int x = Math.Abs(a - b);
        int y = x * 2;
        if (y >= c && y % 2 == 0 && x != 1 && a <= y && b <= y)
            return c + x > y ? c - x : c + x;
        return -1;
    }
}