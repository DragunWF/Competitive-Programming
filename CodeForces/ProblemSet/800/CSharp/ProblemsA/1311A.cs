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
            int a = int.Parse(v[0]);
            int b = int.Parse(v[1]);
            Console.WriteLine(Solve(a, b));
        }
    }

    private static int Solve(int a, int b)
    {
        int moves = 0;
        if (a != b)
        {
            int r = Math.Abs(a - b);
            if (a < b)
                moves = r % 2 != 0 ? 1 : 2;
            else
                moves = r % 2 == 0 ? 1 : 2;
        }
        return moves;
    }
}