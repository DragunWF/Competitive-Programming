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
            int n = int.Parse(Console.ReadLine());
            int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            Console.WriteLine(Solve(n, arr));
        }
    }

    private static int Solve(int n, int[] arr)
    {
        int evenNums = 0;
        int oddNums = 0;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] % 2 != i % 2)
            {
                if (arr[i] % 2 == 0)
                    evenNums++;
                else
                    oddNums++;
            }
        }
        return evenNums == oddNums ? evenNums : -1;
    }
}