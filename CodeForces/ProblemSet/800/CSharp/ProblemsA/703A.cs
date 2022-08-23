using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static string Solve(int n)
    {
        int mishkaWins = 0;
        int chrisWins = 0;

        for (int i = 0; i < n; i++)
        {
            string[] values = Console.ReadLine().Split(' ');
            int m = int.Parse(values[0]);
            int c = int.Parse(values[1]);

            if (m > c)
                mishkaWins++;
            if (c > m)
                chrisWins++;
        }

        if (mishkaWins == chrisWins)
            return "Friendship is magic!^^";
        return mishkaWins > chrisWins ? "Mishka" : "Chris";
    }
}