using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int[] values = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(values));
    }

    private static int GetMinimum(int[] numbers)
    {
        int minimum = numbers[0];
        for (int i = 1; i < numbers.Length; i++)
            if (numbers[i] < minimum)
                minimum = numbers[i];
        return minimum;
    }

    private static int Solve(int[] values)
    {
        int n = values[0];
        int k = values[1];
        int l = values[2];
        int c = values[3];
        int d = values[4];
        int p = values[5];
        int nl = values[6];
        int np = values[7];

        var toasts = new List<int>();
        toasts.Add(k * l / nl);
        toasts.Add(c * d);
        toasts.Add(p / np);

        return GetMinimum(toasts.Select(x => x / n).ToArray());
    }
}