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
            string s = Console.ReadLine();
            Console.WriteLine(Solve(n, s));
        }
    }

    private static string Solve(int n, string s)
    {
        if (s == "00" || s == "11") return "NO";
        return n > 2 ? "NO" : "YES";
    }
}