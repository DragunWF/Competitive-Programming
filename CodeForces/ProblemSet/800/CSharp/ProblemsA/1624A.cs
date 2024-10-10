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
            string n = Console.ReadLine(); // Ignore n
            int[] arr = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            Console.WriteLine(Solve(arr));
        }
    }

    private static int Solve(int[] arr)
    {
        Array.Sort(arr);
        return arr[arr.Length - 1] - arr[0];
    }
}