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
        int minimumCapacity = 0;
        int passengers = 0;
        for (int i = 0; i < n; i++)
        {
            int[] v = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int exiting = v[0];
            int entering = v[1];
            passengers += entering - exiting;
            if (passengers > minimumCapacity)
                minimumCapacity = passengers;
        }
        return minimumCapacity;
    }
}