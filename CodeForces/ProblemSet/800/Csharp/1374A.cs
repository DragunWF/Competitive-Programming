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
        int output = 0;
        while (n > 0)
        {
            if (n % x == y)
            {
                output = n;
                break;
            }
            n--;
        }
        return output;
    }
}