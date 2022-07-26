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
            string[] v = Console.ReadLine().Split(' ');
            int h = int.Parse(v[0]);
            int m = int.Parse(v[1]);
            Console.WriteLine(Solve(h, m));
        }
    }

    private static int Solve(int h, int m)
    {
        return (23 - h) * 60 + 60 - m;
    }
}