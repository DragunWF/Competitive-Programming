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
			int r = int.Parse(Console.ReadLine());
            Console.WriteLine(Solve(r));
        }
	}

	private static string Solve(int r)
    {
		if (r >= 1900)
			return "Division 1";
		if (r >= 1600)
			return "Division 2";
		if (r >= 1400)
			return "Division 3";
		return "Division 4";
    }
}