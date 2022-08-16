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
			string s = Console.ReadLine();
            Console.WriteLine(Solve(s));
        }
	}

	private static string Solve(string s)
	{
		return s.ToLower() == "yes" ? "YES" : "NO";
	}
}