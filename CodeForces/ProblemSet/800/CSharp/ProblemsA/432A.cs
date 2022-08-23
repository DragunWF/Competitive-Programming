using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        string[] nums = Console.ReadLine().Split(' ');
        int n = int.Parse(nums[0]);
        int k = int.Parse(nums[1]);
        int[] p = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n, k, p));
    }

    private static int Solve(int n, int k, int[] p)
    {
        int eligibleMembers = 0;
        for (int i = 0; i < n; i++)
            if (p[i] + k <= 5)
                eligibleMembers++;
        return eligibleMembers / 3;
    }
}