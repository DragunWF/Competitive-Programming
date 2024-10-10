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

    private static int Solve(int n, int[] arr)
    {
        Array.Sort(arr);
        int candiesToEat = 0;
        for (int i = 1; i < n; i++)
            candiesToEat += arr[i] - arr[0];
        return candiesToEat;
    }
}