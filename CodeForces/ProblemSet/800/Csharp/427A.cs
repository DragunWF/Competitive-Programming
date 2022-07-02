using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        var e = Console.ReadLine().Split(" ").Select(x => int.Parse(x)).ToArray();
        Console.WriteLine(Solve(e));
    }

    private static int Solve(int[] e)
    {
        int policemen = 0;
        int untreatedCrimes = 0;
        foreach (int eventNum in e)
        {
            if (eventNum >= 0)
                policemen += eventNum;
            else
            {
                if (policemen > 0)
                    policemen--;
                else
                    untreatedCrimes++;
            }
                
        }
        return untreatedCrimes;
    }
}