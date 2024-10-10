using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int[] d = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        Console.WriteLine(Solve(d));
    }

    private static int Solve(int[] d)
    {
        int[] distances =
        {
            d[0] + d[1] + d[2],
            d[0] * 2 + d[1] * 2,
            d[1] * 2 + d[2] * 2,
            d[0] * 2 + d[2] * 2
        };
        int minDistance = distances[0];
        for (int i = 1; i < distances.Length; i++)
            if (distances[i] < minDistance)
                minDistance = distances[i];
        return minDistance;
    }
}