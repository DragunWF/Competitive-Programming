using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int q = int.Parse(Console.ReadLine());
        for (int i = 0; i < q; i++)
        {
            int n = int.Parse(Console.ReadLine());
            long[] a = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();
            Console.WriteLine(Solve(n, a));
        }
    }

    private static long GetMin(Dictionary<long, long> dict)
    {
        long[] values = new long[dict.Count];
        int j = 0;
        foreach (var pair in dict)
        {
            values[j] = pair.Key;
            j++;
        }

        long minNum = values[0];
        for (int i = 1; i < values.Length; i++)
            if (values[i] < minNum)
                minNum = values[i];

        return dict[minNum];
    }

    private static long Solve(int n, long[] a)
    {
        var pricesAndSum = new Dictionary<long, long>();
        long[] uniqueNums = new HashSet<long>(a).ToArray();
        long initialSum = a.Aggregate((a, n) => a + n);

        for (int i = 0; i < uniqueNums.Length; i++)
        {
            long[] newArr = new long[n];
            for (int j = 0; j < n; j++)
                newArr[j] = uniqueNums[i];

            long newSum = newArr.Aggregate((a, n) => a + n);
            if (newSum >= initialSum)
                pricesAndSum.Add(newSum, uniqueNums[i]);
        }

        return GetMin(pricesAndSum);
    }
}