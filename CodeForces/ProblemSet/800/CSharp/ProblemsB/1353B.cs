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
            string[] values = Console.ReadLine().Split(' ');
            int n = int.Parse(values[0]);
            int k = int.Parse(values[1]);
            Console.WriteLine(Solve(n, k));
        }
    }

    private static int[] ConvertToIntArrayAndSort(string str)
    {
        int[] arr = str.Split(' ').Select(x => int.Parse(x)).ToArray();
        Array.Sort(arr);
        return arr;
    }

    private static int Solve(int n, int k)
    {
        int[] swappedArr = new int[n];
        int[] a = ConvertToIntArrayAndSort(Console.ReadLine());
        int[] b = ConvertToIntArrayAndSort(Console.ReadLine());
        Array.Reverse(b);

        for (int i = 0; i < n; i++)
            swappedArr[i] = i + 1 > k ? a[i] : Math.Max(a[i], b[i]);

        return swappedArr.Aggregate((a, n) => a + n);
    }
}