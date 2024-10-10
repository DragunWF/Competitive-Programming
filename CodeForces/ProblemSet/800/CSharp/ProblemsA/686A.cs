using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        string[] v = Console.ReadLine().Split(' ');
        int n = int.Parse(v[0]);
        long x = long.Parse(v[1]);
        Console.WriteLine(Solve(n, x));
    }

    private static string Solve(int n, long x)
    {
        int distressedKids = 0;
        for (int i = 0; i < n; i++)
        {
            string[] v = Console.ReadLine().Split(' ');
            int icecreams = int.Parse(v[1]);
            if (v[0] == "+")
                x += icecreams;
            else
            {
                if (icecreams > x)
                    distressedKids++;
                else
                    x -= icecreams;
            }
        }
        return string.Format("{0} {1}", x, distressedKids);
    }
}