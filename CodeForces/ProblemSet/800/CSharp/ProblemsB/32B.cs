using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        string borzeCode = Console.ReadLine();
        Console.WriteLine(Solve(borzeCode));
    }

    private static string Solve(string code)
    {
        var decoded = new List<char>();
        for (int i = 0; i < code.Length; i++)
        {
            if (code[i] == '-' && i + 1 != code.Length)
            {
                char nextChar = code[i + 1];
                decoded.Add(nextChar == '.' ? '1' : '2');
                i++;
            }
            else
                decoded.Add('0');
        }
        return string.Join("", decoded);
    }
}