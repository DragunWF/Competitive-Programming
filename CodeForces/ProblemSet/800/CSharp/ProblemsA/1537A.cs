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
            float n = float.Parse(Console.ReadLine());
            float[] a = Console.ReadLine().Split(' ').Select(float.Parse).ToArray();
            Console.WriteLine(Solve(n, a));
        }
    }

    private static int Solve(float n, float[] a)
    {
        float arrSum = a.Aggregate((a, n) => a + n);
        if (arrSum / n == 1)
            return 0;
        int diff = (int)(arrSum - n);
        return arrSum > 0 && diff > 0 ? diff : 1;
    }
}