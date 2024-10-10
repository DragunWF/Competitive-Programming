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
        int moves = 0;
        int evenNums = 0;
        int oddNums = 0;
        bool parityCog = arr[0] % 2 == 0;

        for (int i = 1; i < n; i++)
        {
            if (arr[i] % 2 == 0)
            {
                evenNums++;
                if (parityCog)
                    moves++;
            }
            if (arr[i] % 2 != 0)
            {
                oddNums++;
                if (!parityCog)
                    moves++;
            }
            parityCog = !parityCog;
        }

        if (n % 2 == 0 && evenNums != oddNums || 
            n % 2 != 0 && Math.Abs(evenNums - oddNums) > 1)
            return -1;

        return moves;
    }
}