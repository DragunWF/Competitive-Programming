using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int x = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(x));
    }

    private static int Solve(int x)
    {
        int[] divisors = new int[5] { 100, 20, 10, 5, 1 };
        int bills = 0;
        while (x > 0)
        {
            foreach (int divisor in divisors)
            {
                if (x >= divisor)
                {
                    int r = x / divisor;
                    x -= r * divisor;
                    bills += r;
                    break;
                }
            }
        }
        return bills;
    }
}