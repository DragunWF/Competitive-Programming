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
        bool suspicious = false;
        var tasks = new List<char>();
        char lastTask = '0';

        for (int i = 0; i < n; i++)
        {
            if (s[i] != lastTask && tasks.Contains(s[i]))
            {
                suspicious = true;
                break;
            }

            if (!tasks.Contains(s[i]))
                tasks.Add(s[i]);
            lastTask = s[i];
        }

        return suspicious ? "NO" : "YES";
    }
}