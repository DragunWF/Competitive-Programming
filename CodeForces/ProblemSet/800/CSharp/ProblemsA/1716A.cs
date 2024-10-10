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

	private static int GetDividedDistance(int divisor, int n)
    {
		return n % divisor == 0 ? n / divisor : 0;
    }

	private static int Solve(int n)
	{
		if (n == 1)
			return 2;

		int r = n / 3 + 1;
		int a = GetDividedDistance(3, n);
		int b = GetDividedDistance(2, n);

		int[] values = new int[3] { a, b, r };
		int[] filteredValues = values.Where(x => x != 0).ToArray();

		int minValue = filteredValues[0];
		for (int i = 1; i < filteredValues.Length; i++)
			if (filteredValues[i] < minValue)
				minValue = filteredValues[i];

		return minValue;
	}
}