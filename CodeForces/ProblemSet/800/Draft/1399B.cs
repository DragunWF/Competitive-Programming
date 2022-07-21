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
            string n = Console.ReadLine(); // Ignore n
            int[] a = ConvertToIntArrayAndSort(Console.ReadLine());
            int[] b = ConvertToIntArrayAndSort(Console.ReadLine());
            Console.WriteLine(Solve(a, b));
        }
    }

    private static int[] ConvertToIntArrayAndSort(string str)
    {
        int[] arr = str.Split(' ').Select(x => int.Parse(x)).ToArray();
        Array.Sort(arr);
        return arr;
    }

    private static int GetMovesToEqualize(int[] arr)
    {
        int moves = 0;
        Array.Sort(arr);
        for (int i = 1; i < arr.Length; i++)
            moves += arr[i] - arr[0];
        return moves;  
    }

    private static int Solve(int[] a, int[] b)
    {
        int movesA = GetMovesToEqualize(a);
        int movesB = GetMovesToEqualize(b);
        return movesA + movesB;
    }
}