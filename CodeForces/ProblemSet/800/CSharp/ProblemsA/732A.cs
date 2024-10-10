using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        var n = Console.ReadLine().Split(" ");
        int k = int.Parse(n[0]);
        int r = int.Parse(n[1]);
        Console.WriteLine(Solve(k, r));
    }

    private static int Solve(int k, int r)
    {
        string strK = k.ToString();
        int lastNum = int.Parse(strK[strK.Length - 1].ToString());
        int initialShovelValue = k;
        int shovels = 1;

        while (lastNum != r && lastNum != 0)
        {
            shovels++;
            k += initialShovelValue;
            strK = k.ToString();
            lastNum = int.Parse(strK[strK.Length - 1].ToString());
        }

        return shovels;
    }
}