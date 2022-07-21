using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int[] arr = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        string str = Console.ReadLine();
        Console.WriteLine(Solve(arr, str));
    }

    private static int Solve(int[] arr, string str)
    {
        int caloriesBurned = 0;
        foreach (char chr in str)
        {
            int charIndex = int.Parse(chr.ToString()) - 1;
            caloriesBurned += arr[charIndex];
        }
        return caloriesBurned;
    }
}