using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] c = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n, c));
    }

    private static int Solve(int n, int[] c)
    {
        int burles = 0;
        Array.Sort(c);
        for (int i = 0; i < (n - 1); i++)
            burles += c[n - 1] - c[i];
        return burles;
    }
}