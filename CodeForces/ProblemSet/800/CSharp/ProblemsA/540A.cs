using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string original = Console.ReadLine();
        string password = Console.ReadLine();
        Console.WriteLine(Solve(n, original, password));
    }

    private static int Solve(int n, string o, string p)
    {
        int actions = 0;
        for (int i = 0; i < n; i++)
        {
            int methodOne = Math.Abs(o[i] - p[i]);
            int methodTwo = Math.Min(o[i], p[i]) + 10 - Math.Max(o[i], p[i]);
            actions += Math.Min(methodOne, methodTwo);
        }
        return actions;
    }
}