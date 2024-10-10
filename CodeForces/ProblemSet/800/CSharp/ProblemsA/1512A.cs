using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            Console.WriteLine(Solve(n, a));
        }
    }
    
    private static int Solve(int n, int[] a)
    {
        for (int i = 1; i < n; i++)
            if (a[i] != a[0])
                return i + 1;
        return 1;
    }
}