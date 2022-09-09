using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
	private static void Main()
	{
		int n = int.Parse(Console.ReadLine());
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        Console.WriteLine(Solve(n, arr));
	}

	private static int Solve(int n, int[] arr)
    {
		int subLength = 1;
		int maxSubLength = subLength;
		for (int i = 1; i < n; i++)
        {
			if (arr[i] > arr[i - 1])
				subLength++;
			else
				subLength = 1;
			if (subLength > maxSubLength)
				maxSubLength = subLength;
        }
		return maxSubLength;
    }
}