using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int[] n = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int[] n)
    {
        Array.Sort(n);
        return n[2] - n[0];
    }
}
