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
        int parenthesis = 0;
        int remainingChars = 0;
        for (int i = n - 1; i >= (n - 1) / 2; i--)
        {
            if (s[i] == ')')
                parenthesis++;
            else
            {
                remainingChars = n - i + 1;
                break;
            }
        }
        return parenthesis > remainingChars ? "Yes" : "No";
    }
}