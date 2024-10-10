using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    private static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static int Solve(int n)
    {
        int g = 0;
        string previousMagnet = "";
        for (int i = 0; i < n; i++)
        {
            string m = Console.ReadLine();
            if (m != previousMagnet)
                g++;
            previousMagnet = m;
        }
        return g;
    }
}