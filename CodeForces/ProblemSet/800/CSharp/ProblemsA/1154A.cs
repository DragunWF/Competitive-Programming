using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        var n = Console.ReadLine().Split(" ").Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n));
    }

    private static string Solve(int[] n)
    {
        var pairwiseSums = new List<int>();
        Array.Sort(n);
        for (int i = 0; i < n.Length - 1; i++)
            pairwiseSums.Add(n[n.Length - 1] - n[i]);
        return string.Join(" ", pairwiseSums);
    }
}