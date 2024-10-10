using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        string n = Console.ReadLine(); // Ignore n
        string s = Console.ReadLine();
        Console.WriteLine(Solve(s));
    }

    private static string Solve(string s)
    {
        var alphabetsLength = "abcdefghijklmnopqrstuvwxyz".ToCharArray().Length;
        var distinctCount = new HashSet<char>(s.ToLower().ToCharArray()).Count;
        return distinctCount - alphabetsLength == 0 ? "YES" : "NO";
    }
}