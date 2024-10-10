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
            Console.WriteLine(Solve(n));
        }
    }

    private static int CountChanges(int org, int num)
    {
        int count = 0;
        string x = num.ToString();
        string y = org.ToString();

        if (x.Length != y.Length)
            return 10000;

        for (int i = 0; i < y.Length; i++)
            if (x[i] != y[i])
                count++;

        return count;
    }

    private static int Solve(int n)
    {
        if (n % 7 == 0)
            return n;

        int m = n - (n % 7);
        int a = n;
        while (a % 7 != 0)
            a++;
        if (m < 10)
            return a;

        int x = CountChanges(n, m);
        int y = CountChanges(n, a);
        return x < y ? m : a;
    }
}