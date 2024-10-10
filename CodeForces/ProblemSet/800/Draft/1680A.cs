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
			int[] v = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
			int l1 = v[0];
			int r1 = v[1];
			int l2 = v[2];
			int r2 = v[3];
            Console.WriteLine(Solve(l1, r1, l2, r2));
        }
	}

	private static int Solve(int l1, int r1, int l2, int r2)
	{
		if (l2 > r1 || l1 > r2)
			return l1 + l2;
		if (r1 > r2 || r2 > r1)
			return Math.Max(l1, l2);
		return l1;
	}
}