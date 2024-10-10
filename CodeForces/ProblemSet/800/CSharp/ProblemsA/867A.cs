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
		bool inSanFrancisco = s[0] == 'F';
		int sanFranciscoFlights = 0;

		for (int i = 1; i < n; i++)
        {
			if (s[i] == 'S' && inSanFrancisco)
            {
				sanFranciscoFlights--;
                inSanFrancisco = false;
            }
			else if (s[i] == 'F' && !inSanFrancisco)
            {
				sanFranciscoFlights++;
                inSanFrancisco = true;
            }
        }

		return sanFranciscoFlights > 0 ? "YES" : "NO";
    }
}