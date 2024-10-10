using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
	private static void Main()
	{
		string[] v = Console.ReadLine().Split(' ');
		int n = int.Parse(v[0]);
		int m = int.Parse(v[1]);
		Console.WriteLine(Solve(n, m));
	}

	private static List<int> GetPrimeNumbers()
    {
		List<int> primeNumbers = new List<int>();
		List<int> nonPrimeNumbers = new List<int>();
		const int primeLength = 50;

		for (int i = 2; i <= primeLength; i++)
        {
			for (int j = 2; j <= primeLength; j++)
            {
				int r = i * j;
				if (r > primeLength)
					break;
				nonPrimeNumbers.Add(r);
            }
        }

		for (int i = 2; i <= primeLength; i++)
			if (!nonPrimeNumbers.Contains(i))
				primeNumbers.Add(i);

		return primeNumbers;
    }

	private static string Solve(int n, int m)
    {
		List<int> primes = GetPrimeNumbers();
		bool isNextPrime = false;

		if (primes.Contains(m))
        {
			for (int i = 0; i < primes.Count; i++)
            {
				if (primes[i] == n)
                {
					if (i + 1 != primes.Count && primes[i + 1] == m)
						isNextPrime = true;
					break;
                }
            }
        }

		return isNextPrime ? "YES" : "NO";
    }
}