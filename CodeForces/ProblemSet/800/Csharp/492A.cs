using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int n)
    {
        int height = 0;
        while (n > 0)
        {
            for (int i = 1; i <= height + 1; i++)
                n -= i;

            if (n >= 0)
                height++;
        }
        return height;
    }
}