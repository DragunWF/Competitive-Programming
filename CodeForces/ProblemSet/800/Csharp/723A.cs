using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int[] n = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int[] n)
    {
        int maxDistance = n[0];
        int minDistance = n[0];
        foreach (int distance in n)
        {
            if (distance > maxDistance)
                maxDistance = distance;
            if (distance < minDistance)
                minDistance = distance;
        }
        return maxDistance - minDistance;
    }
}
