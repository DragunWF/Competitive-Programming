using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        var nums = Console.ReadLine().Split(" ");
        int n = int.Parse(nums[0]);
        int k = int.Parse(nums[1]);
        Console.WriteLine(Solve(n, k));
    }

    private static int SumArray(List<int> arr)
    {
        int sum = 0;
        foreach (int num in arr)
            sum += num;
        return sum;
    }

    private static int Solve(int n, int k)
    {
        int timeForParty = 60 * 4;
        var multipliers = new List<int>();

        for (int i = 1; i <= n; i++)
            multipliers.Add(i * 5);

        while (SumArray(multipliers) + k > timeForParty)
        {
            multipliers.RemoveAt(multipliers.Count - 1);
            n -= 1;
        }

        return n;
    }
}