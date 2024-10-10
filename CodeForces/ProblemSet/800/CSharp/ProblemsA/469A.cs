using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] x = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        int[] y = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n, x, y));
    }

    private static string Solve(int n, int[] x, int[] y)
    {
        List<int> levelsPassed = new List<int>();
        for (int i = 0; i < 2; i++)
        {
            int[] array = i == 0 ? x : y;
            for (int j = 1; j < array.Length; j++)
                levelsPassed.Add(array[j]);
        }
        HashSet<int> uniqueLevels = new HashSet<int>(levelsPassed);
        return n - uniqueLevels.Count == 0 ? "I become the guy." : "Oh, my keyboard!";
    }
}