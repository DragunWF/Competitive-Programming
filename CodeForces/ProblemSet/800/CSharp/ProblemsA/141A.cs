using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        string a = Console.ReadLine();
        string b = Console.ReadLine();
        string c = Console.ReadLine();
        Console.WriteLine(Solve(a, b, c));
    }

    private static string Solve(string a, string b, string c)
    {
        char[] x = string.Format("{0}{1}", a, b).ToCharArray();
        char[] t = c.ToCharArray();
        Array.Sort(x);
        Array.Sort(t);
        return string.Join("", x) == string.Join("", t) ? "YES" : "NO";
    }
}