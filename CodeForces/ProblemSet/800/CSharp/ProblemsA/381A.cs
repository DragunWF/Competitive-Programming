using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var a = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToList();
        Console.WriteLine(Solve(n, a));
    }

    private static string Solve(int n, List<int> a)
    {
        int serejaPoints = 0;
        int dimaPoints = 0;

        for (int i = 0; i < n; i++)
        {
            int lastIndex = a.Count - 1;
            int points = Math.Max(a[0], a[lastIndex]);

            if ((i + 1) % 2 == 0)
                dimaPoints += points;
            else
                serejaPoints += points;

            a.RemoveAt(points == a[0] ? 0 : lastIndex);
        }

        return string.Format("{0} {1}", serejaPoints, dimaPoints);
    }
}