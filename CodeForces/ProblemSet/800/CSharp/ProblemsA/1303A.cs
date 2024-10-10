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
            string s = Console.ReadLine();
            Console.WriteLine(Solve(s));
        }
    }

    private static int Solve(string s)
    {
        int operations = 0;
        int tempZeroCount = 0;
        bool passedDigitOne = false;
        for (int i = 0; i < s.Length; i++)
        {
            switch (s[i])
            {
                case '1':
                    if (passedDigitOne && tempZeroCount > 0)
                    {
                        operations += tempZeroCount;
                        tempZeroCount = 0;
                    }
                    passedDigitOne = true;
                    break;
                case '0':
                    if (passedDigitOne)
                        tempZeroCount++;
                    break;
            }
        }
        return operations;
    }
}