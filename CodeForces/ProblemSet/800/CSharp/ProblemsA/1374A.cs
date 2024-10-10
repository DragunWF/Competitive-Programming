using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            string[] nums = Console.ReadLine().Split(' ');
            int x = int.Parse(nums[0]);
            int y = int.Parse(nums[1]);
            int n = int.Parse(nums[2]);
            Console.WriteLine(Solve(x, y, n));
        }
    }

    private static int Solve(int x, int y, int n)
    {
        int d = n / x;
        int r = x * d + y;
        return r > n ? r - x : r;
    }
}