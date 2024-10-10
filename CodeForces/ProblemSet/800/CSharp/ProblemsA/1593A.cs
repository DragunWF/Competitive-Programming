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
			Console.WriteLine(Solve(v));
        }
	}

	private static int CalculateVotes(int votes, int maxVotes, bool duplicates)
    {
		if (votes == maxVotes)
			return duplicates ? 1 : 0;
		return maxVotes - votes + 1;
    }

	private static string Solve(int[] candidates)
	{
		int maxVotes = 0;
		foreach (int votes in candidates)
			if (votes > maxVotes)
				maxVotes = votes;

		bool duplicateMaxVotes = candidates.Where(x => x == maxVotes).Count() > 1;
        int[] output = candidates
			.Select(x => CalculateVotes(x, maxVotes, duplicateMaxVotes))
			.ToArray();
		return string.Format("{0} {1} {2}", output[0], output[1], output[2]);
	}
}