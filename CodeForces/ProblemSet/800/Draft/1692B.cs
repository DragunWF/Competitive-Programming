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
            int[] arr = intArr(Console.ReadLine());
            Console.WriteLine("Output: " + Solve(arr, n));
        }
    }

    private static int[] intArr(string input)
    {
        return input.Split(' ').Select(int.Parse).ToArray();
    }

    private static int Solve(int[] arr, int n)
    {
        int setLength = new HashSet<int>(arr).Count;
        int modulus = n % setLength;

        if (setLength == 1 && n == 2)
            return 0;

        return modulus == 0 ? setLength : modulus;
    }
}