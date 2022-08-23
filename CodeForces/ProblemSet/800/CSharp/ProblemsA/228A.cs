using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int[] n = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int[] n)
    {
        var set = new HashSet<int>(n);
        return n.Length - set.Count;
    }
}