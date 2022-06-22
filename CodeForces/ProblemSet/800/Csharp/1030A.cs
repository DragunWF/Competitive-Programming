using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    private static void Main()
    {
        string n = Console.ReadLine(); // Ignore n
        int[] a = Console.ReadLine().Split(" ").Select(x => Convert.ToInt32(x)).ToArray();
        Console.WriteLine(Solve(a));
    }

    private static string Solve(int[] a)
    {
        return a.Contains(1) ? "HARD" : "EASY";
    }
}