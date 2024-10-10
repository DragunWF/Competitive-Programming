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
            int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Console.WriteLine(Solve(n, arr));
        }
    }

    private static int[] FindIndexes(int n, int[] arr)
    {
        int maximum = arr[0];
        int minimum = arr[0];
        int maximumIndex = 0;
        int minimumIndex = 0;

        for (int i = 1; i < n; i++)
        {
            if (arr[i] > maximum)
            {
                maximum = arr[i];
                maximumIndex = i;
            }
            if (arr[i] < minimum)
            {
                minimum = arr[i];
                minimumIndex = i;
            }
        }

        return new int[2] { minimumIndex, maximumIndex };
    }

    private static int Solve(int n, int[] arr)
    {
        int[] indexes = FindIndexes(n, arr);
        int minIndex = indexes[0];
        int maxIndex = indexes[1];

        int a = Math.Min(minIndex + 1, n - minIndex);
        int b = Math.Min(maxIndex + 1, n - maxIndex);
        int c = Math.Abs(maxIndex - minIndex);

        return c < Math.Max(a, b) ? c + Math.Min(a, b) : a + b;
    }
}