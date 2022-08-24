using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Solve(n);
    }

    private static void Solve(int n)
    {
        string[] seats = new string[n];
        bool possible = false;
        for (int i = 0; i < n; i++)
        {
            string[] row = Console.ReadLine().Split('|');
            if (!possible)
            {
                if (row[0] == "OO")
                {
                    row[0] = "++";
                    possible = true;
                }
                else if (row[1] == "OO")
                {
                    row[1] = "++";
                    possible = true;
                }
            }
            seats[i] = string.Join('|', row);
        }

        Console.WriteLine(possible ? "YES" : "NO");
        if (possible)
            foreach (string row in seats)
                Console.WriteLine(row);
    }
}