using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.ReadLine(); // Will not be needed
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int n)
    {
        return n + 1;
    }
}