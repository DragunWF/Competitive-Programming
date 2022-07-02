using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        var n = Console.ReadLine().Split(" ");
        int a = int.Parse(n[0]);
        int b = int.Parse(n[1]);
        Console.WriteLine(Solve(a, b));
    }

    private static string Solve(int a, int b)
    {
        int daysLeft = a > b ? b : a;
        int pairsLeft = Math.Abs(a - b) / 2;
        return string.Format("{0} {1}", daysLeft, pairsLeft);
    }
}