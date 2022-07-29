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
            int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Console.WriteLine(Solve(arr));
        }
	}

	private static int Solve(int[] arr)
    {
		int participantsAhead = 0;
		for (int i = 1; i < arr.Length; i++)
			if (arr[i] > arr[0])
				participantsAhead++;
		return participantsAhead;
    }
}