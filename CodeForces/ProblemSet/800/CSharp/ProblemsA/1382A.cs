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
            int[] v = ConvertToIntArray(Console.ReadLine());
            int[] a = ConvertToIntArray(Console.ReadLine());
            int[] b = ConvertToIntArray(Console.ReadLine());
            int n = v[0];
            int m = v[1];
            Solve(n, m, a, b);
        }
    }

    private static int[] ConvertToIntArray(string str)
    {
        return str.Split(' ').Select(int.Parse).ToArray();
    }

    private static int GetMin(List<int> arr)
    {
        int min = arr[0];
        for (int i = 1; i < arr.Count; i++)
            if (arr[i] < min)
                min = arr[i];
        return min;
    }

    private static void Solve(int n, int m, int[] a, int[] b)
    {
        var sub = new List<int>();
        int[] x = n > m ? a : b;
        int[] y = x == a ? b : a;

        foreach (int num in x)
            if (y.Contains(num))
                sub.Add(num);

        if (sub.Count > 0)
        {
            Console.WriteLine("YES");
            Console.WriteLine("1 {0}", GetMin(sub));
        }
        else
            Console.WriteLine("NO");
    }
}