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
		int sum = 0;
		for (int i = 0; i < s.Length; i++)
        {
			int num = int.Parse(s[i].ToString());
			sum += i <= 2 ? num : -num;
        }
		return sum == 0 ? "YES" : "NO";
	}
}