using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] a = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n, a));
    }

    private static int Solve(int n, int[] a)
    {
        int minNumIndex = FindNum(a, true);
        int maxNumIndex = FindNum(a, false);
        int minNumMoves = Math.Abs(minNumIndex + 1 - a.Length);
        return minNumMoves + maxNumIndex - (maxNumIndex > minNumIndex ? 1 : 0);
    }

    private static int FindNum(int[] a, bool findMin)
    {
        int num = a[0];
        int index = 0;
        for (int i = 0; i < a.Length; i++)
        {
            if (findMin && a[i] <= num || !findMin && a[i] > num)
            {
                num = a[i];
                index = i;
            }
        }
        return index;
    }
}
