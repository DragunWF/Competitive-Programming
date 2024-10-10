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
            int[] arr = intArr(Console.ReadLine());
            Console.WriteLine(Solve(arr, n));
        }
    }

    private static int[] intArr(string input)
    {
        return input.Split(' ').Select(int.Parse).ToArray();
    }

    private static int Solve(int[] arr, int n)
    {
        int maxSeq = 1;
        int currentSeq = 1;

        for (int i = 1; i < n; i++)
        {
            if (arr[i] == arr[i - 1])
                currentSeq++;
            else
                currentSeq = 1;

            if (currentSeq > maxSeq)
                maxSeq = currentSeq;
        }

        return maxSeq;
    }
}