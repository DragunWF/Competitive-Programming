using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            Console.WriteLine(Solve(n, arr));
        }
    }

    private static int Solve(int n, int[] arr)
    {
        var strengths = new List<int>();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i != j)
                    strengths.Add(Math.Abs(arr[i] - arr[j]));
            }
        }

        strengths.Sort();
        return strengths[0];
    }
}