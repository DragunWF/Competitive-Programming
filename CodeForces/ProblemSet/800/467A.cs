using System;
using System.Collections;
using System.Collections.Generic;

public class Program
{
    private static void Main()
    {
        int r = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(Solve(r));
    }

    private static int Solve(int r)
    {
        int a = 0;
        for (int i = 0; i < r; i++)
        {
            string[] c = Console.ReadLine().Split(" ");
            int q = Convert.ToInt32(c[0]);
            int p = Convert.ToInt32(c[1]);
            if (p - q >= 2)
                a++;
        }
        return a;
    }
}