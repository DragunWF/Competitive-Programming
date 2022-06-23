using System;
using System.Collections;
using System.Collections.Generic;

public class Program
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static string Solve(int n)
    {
        var output = new List<string>();
        for (int i = 1; i <= n; i++)
        {
            string phrase = i % 2 == 0 ? "I love" : "I hate";
            phrase += i == n ? " it" : " that";
            output.Add(phrase);
        }
        return string.Join(' ', output);
    }
}