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
            string[] arr = Console.ReadLine().Split(' ');
            int a = int.Parse(arr[0]);
            int b = int.Parse(arr[1]);
            Console.WriteLine(Solve(a, b));
        }
    }

    private static int Solve(int a, int b)
    {
        if (b > a)
            return b - a;
        return a % b == 0 ? 0 : Math.Abs(a % b - b);
    }
}