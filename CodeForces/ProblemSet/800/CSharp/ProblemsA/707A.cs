using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        string[] values = Console.ReadLine().Split(' ');
        int n = int.Parse(values[0]);
        Console.WriteLine(Solve(n));
    }

    private static string Solve(int n)
    {
        string[] colorfulColors = new string[3] { "C", "M", "Y" };
        int colorCount = 0;

        for (int i = 0; i < n; i++)
        {
            string[] colors = Console.ReadLine().Split(' ');
            colorCount += colors.Where(x => colorfulColors.Contains(x)).Count();
        }

        return colorCount > 0 ? "#Color" : "#Black&White";
    }
}