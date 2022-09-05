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
            Console.ReadLine();
            int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Console.WriteLine(Solve(arr));
        }
    }

    private static string Solve(int[] arr)
    {
        int[] restored = new HashSet<int>(arr).ToArray();
        return String.Join(' ', restored);
    }
}