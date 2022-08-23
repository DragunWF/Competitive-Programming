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
            int n = int.Parse(Console.ReadLine());
            Console.WriteLine(Solve(n));
        }
    }

    private static string Solve(int n)
    {
        string converted = n.ToString();
        var nums = new List<int>();

        for (int i = 0; i < converted.Length; i++)
        {
            string numStr = converted[i].ToString();
            if (int.Parse(numStr) > 0)
            {
                var roundedNum = new List<string>();
                roundedNum.Add(numStr);
                for (int j = 0; j < converted.Length - (i + 1); j++)
                    roundedNum.Add("0");
                nums.Add(int.Parse(string.Join("", roundedNum)));
            }
        }

        Console.WriteLine(nums.Count);
        return string.Join(" ", nums);
    }
}