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
            char[] s = Console.ReadLine().ToCharArray();
            char c = char.Parse(Console.ReadLine());
            Console.WriteLine(Solve(c, s));
        }
    }

    private static string Solve(char c, char[] s)
    {
        int a = 0;
        foreach (char item in s)
        {
            a++;
            if (item == c)
            {
                a = 0;
                if (a % 2 != 0)
                    return "NO";
            }
        }
        return a % 2 == 0 ? "YES" : "NO";
    }
}