using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        string s = Console.ReadLine();
        Console.WriteLine(Solve(n, s));
    }

    private static string Solve(int n, string s)
    {
        var word = new List<char>();
        int letterCount = 0;
        for (int i = 0; i < n; i++)
        {
            letterCount++;
            if (letterCount > word.Count)
            {
                word.Add(s[i]);
                letterCount = 0;
            }
        }
        return String.Join("", word);
    }
}