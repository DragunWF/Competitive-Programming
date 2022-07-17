using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int k = int.Parse(Console.ReadLine());
            Console.WriteLine(Solve(k));
        }
    }

    private static char GetLastNumber(int n)
    {
        string convertedNum = n.ToString();
        return convertedNum[convertedNum.Length - 1];
    }

    private static int Solve(int k)
    {
        int i = 0;
        int n = 0;
        while (i < k)
        {
            n++;
            char lastNum = GetLastNumber(n);
            if (!(lastNum == '3' || n % 3 == 0))
                i++;
        }
        return n;
    }
}