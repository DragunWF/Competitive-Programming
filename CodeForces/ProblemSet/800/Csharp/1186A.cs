using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
	private static void Main()
	{
		int[] v = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
		int n = v[0];
		int m = v[1];
		int k = v[2];
        Console.WriteLine(Solve(n, m, k));
	}

	private static string Solve(int n, int m, int k)
	{
		return Math.Min(m, k) >= n ? "YES" : "NO";
	}
}