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
            string[] n = Console.ReadLine().Split(' ');
            int a = int.Parse(n[0]);
            int b = int.Parse(n[1]);
            Console.WriteLine(Solve(a, b));
        }
    }

    private static int Solve(int a, int b)
    {
        int output = 0;
        if (a != b)
        {
            int x = a > b ? a : b;
            int y = a < b ? a : b;
            int d = x - y;
            output = d / 10 + (d % 10 != 0 ? 1 : 0);
        }
        return output;
    }
}