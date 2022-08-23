using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        string input = Console.ReadLine();
        string[] arr = input.Substring(1, input.Length - 2).Split(", ");
        Console.WriteLine(Solve(arr));
    }

    private static int Solve(string[] arr)
    {
        if (string.IsNullOrWhiteSpace(arr[0]))
            return 0;
        return new HashSet<string>(arr).Count;
    }
}