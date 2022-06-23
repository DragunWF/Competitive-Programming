using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int k = int.Parse(Console.ReadLine());
        int l = int.Parse(Console.ReadLine());
        int m = int.Parse(Console.ReadLine());
        int n = int.Parse(Console.ReadLine());
        int d = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(k, l, m, n, d));
    }

    private static int Solve(int k, int l, int m, int n, int d)
    {
        int output = 0;
        int[] physical = new int[4] { k, l, m, n };
        for (int i = 1; i <= d; i++)
        {
            foreach (int num in physical)
            {
                if (i % num == 0)
                {
                    output++;
                    break;
                }
            }
        }
        return output;
    }
}