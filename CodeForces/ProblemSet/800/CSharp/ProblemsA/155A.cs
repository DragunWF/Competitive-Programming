using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] c = Console.ReadLine().Split(" ").Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n, c));
    }

    private static int Solve(int n, int[] c)
    {
        int amazingContests = 0;
        int bestPerformance = c[0];
        int worstPerformance = c[0];

        for (int i = 1; i < n; i++)
        {
            if (c[i] > bestPerformance)
            {
                bestPerformance = c[i];
                amazingContests++;
            } 
            else if (c[i] < worstPerformance)
            {
                worstPerformance = c[i];
                amazingContests++;
            }
        }

        return amazingContests;
    }
}