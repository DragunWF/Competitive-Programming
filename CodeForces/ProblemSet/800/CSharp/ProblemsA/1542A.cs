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
			int[] arr = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
            Console.WriteLine(Solve(n, arr));
        }
	}

	private static string Solve(int n, int[] arr)
    {
		int oddElementsTotal = 0;
		for (int i = 0; i < n * 2; i++)
			if (arr[i] % 2 != 0)
				oddElementsTotal++;
		return oddElementsTotal == n ? "Yes" : "No";
    }
}