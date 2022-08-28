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
            Console.WriteLine(Solve(n));
        }
    }

    private static int Solve(int n)
    {
        var athletes = new List<int>();
        int participants = (int)Math.Pow(2, n);
        for (int i = 1; i <= participants; i++)
            athletes.Add(i);

        while (athletes.Count > 1)
        {
            var remaining = new List<int>();
            for (int i = 0; i < athletes.Count; i += 2)
            {
                int sum = athletes[i] + athletes[i + 1];
                if (sum % 2 == 0)
                    remaining.Add(Math.Max(athletes[i], athletes[i + 1]));
                else
                    remaining.Add(Math.Min(athletes[i], athletes[i + 1]));
            }
            athletes = remaining;
        }

        return athletes[0];
    }
}