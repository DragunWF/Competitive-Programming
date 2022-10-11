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
            int x = int.Parse(Console.ReadLine());
            int[] doors = intArr(Console.ReadLine());
            Console.WriteLine(Solve(doors, x));
        }
    }

    private static int[] intArr(string input)
    {
        return input.Split(' ').Select(int.Parse).ToArray();
    }

    private static string Solve(int[] doors, int x)
    {
        int firstKey = doors[x - 1];
        int secondKey = firstKey > 0 ? doors[firstKey - 1] : 0;
        return firstKey > 0 && secondKey > 0 ? "YES" : "NO";
    }
}