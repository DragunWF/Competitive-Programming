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
            int[] a = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Console.WriteLine(Solve(n, a));
        }
    }

    private static int GetMin(List<int> intList)
    {
        int minNum = intList[0];
        for (int i = 1; i < intList.Count; i++)
            if (intList[i] < minNum)
                minNum = intList[i];
        return minNum;
    }

    private static int Solve(int n, int[] a)
    {
        var uniques = new List<int>();
        var duplicates = new List<int>();

        for (int i = 0; i < n; i++)
        {
            if (uniques.Contains(a[i]))
            {
                duplicates.Add(a[i]);
                uniques.RemoveAt(uniques.IndexOf(a[i]));
            }
            if (!duplicates.Contains(a[i]))
                uniques.Add(a[i]);
        }

        return uniques.Count > 0 ? Array.IndexOf(a, GetMin(uniques)) + 1 : -1;
    }
}