using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int n)
    {
        var matrix = new int[n][];
        int[] firstArr = new int[n];
        for (int i = 0; i < n; i++)
            firstArr[i] = 1;
        matrix[0] = firstArr;
        
        for (int i = 1; i < n; i++)
        {
            int[] arr = new int[n];
            arr[0] = 1;
            for (int j = 1; j < n; j++)
                arr[j] = arr[j - 1] + matrix[i - 1][j];
            matrix[i] = arr;
        }

        var lastArr = matrix[matrix.Length - 1];
        return lastArr[lastArr.Length - 1];
    }
}