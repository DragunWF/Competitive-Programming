using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        string[] nums = Console.ReadLine().Split(" ");
        int h = int.Parse(nums[0]);
        int w = int.Parse(nums[1]);
        Console.WriteLine(Solve(w, h));
    }

    private static string Solve(int w, int h)
    {
        var snake = new List<string>();
        bool curvedLine = false;
        bool pointRight = true;

        for (int i = 0; i < h; i++)
        {
            var line = new List<string>();
            for (int j = 0; j < w; j++)
            {
                if (curvedLine && j + 1 != (pointRight ? w : 1))
                    line.Add(".");
                else
                    line.Add("#");
            }
            snake.Add(string.Join("", line));

            if (curvedLine)
                pointRight = pointRight ? false : true;
            curvedLine = curvedLine ? false : true;  
        }

        return string.Join("\n", snake);
    }
}