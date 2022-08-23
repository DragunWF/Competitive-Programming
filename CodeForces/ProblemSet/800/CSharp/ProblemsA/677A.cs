using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    private static void Main()
    {
        var values = Console.ReadLine().Split(" ");
        var n = Convert.ToInt32(values[0]);
        var h = Convert.ToInt32(values[1]);
        var arr = Console.ReadLine().Split(" ").Select(x => Convert.ToInt32(x)).ToArray();
        Console.WriteLine(Solve(n, h, arr));
    }

    private static int Solve(int n, int h, int[] arr)
    {
        var b = 0;
        for (int i = 0; i < n; i++)
            if (arr[i] > h) b++;
        return (n - b) + (b * 2);
    }
}
