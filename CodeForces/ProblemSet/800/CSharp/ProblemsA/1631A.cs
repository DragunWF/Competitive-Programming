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
            int[] a = intArr(Console.ReadLine());
            int[] b = intArr(Console.ReadLine());
            Console.WriteLine(Solve(a, b, n));
        }
    }

    private static int[] intArr(string input)
    {
        return input.Split(' ').Select(int.Parse).ToArray();
    }

    private static int GetMaxOrMin(int[] arr, int n, bool isMax)
    {
        int outputNum = arr[0];
        for (int i = 1; i < n; i++)
        {
            if (isMax && arr[i] > outputNum)
                outputNum = arr[i];
            else if (!isMax && arr[i] < outputNum)
                outputNum = arr[i];
        }
        return outputNum;
    }

    private static void DebugArrays(int[] a, int[] b)
    {
        Console.WriteLine("\nOutput:");
        Console.WriteLine(String.Join(" ", a));
        Console.WriteLine(String.Join(" ", b));
    }

    private static int Solve(int[] a, int[] b, int n)
    {
        bool maxArrB = GetMaxOrMin(a, n, true) < GetMaxOrMin(b, n, true);
        
        for (int i = 0; i < n; i++)
        {
            if (maxArrB && a[i] > b[i])
            {
                int tempNumA = a[i];
                a[i] = b[i];
                b[i] = tempNumA;
            } 
            else if (!maxArrB && b[i] > a[i])
            {
                int tempNumB = b[i];
                b[i] = a[i];
                a[i] = tempNumB;
            }
        }

        // DebugArrays(a, b); // for debugging

        int x = GetMaxOrMin(a, n, true);
        int y = GetMaxOrMin(b, n, true);
        return x * y;
    }
}