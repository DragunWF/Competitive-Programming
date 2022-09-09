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
		if (n > 5)
			return "NO";

		const string sortedName = "Timru";
		char[] convertedStr = s.ToCharArray();
		Array.Sort(convertedStr);
		return String.Join("", convertedStr) == sortedName ? "YES" : "NO";
    }
}