using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        // Look I can explain... I was very sleepy when I wrote this :/
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int[] p = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            Console.WriteLine(Solve(p));
        }
    }

    private static bool CheckIncluded(int[] strongest, int[] group)
    {
        return group.Contains(strongest[0]) || group.Contains(strongest[1]);
    }

    private static string Solve(int[] p)
    {
        int[] g1 = { p[0], p[1] };
        int[] g2 = { p[2], p[3] };
        Array.Sort(p);

        int[] sg = { p[2], p[3] };
        return CheckIncluded(sg, g1) && CheckIncluded(sg, g2) ? "YES" : "NO";
    }
}