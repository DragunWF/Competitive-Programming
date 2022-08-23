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
            Console.ReadLine(); // Empty line according to test cases
            Console.WriteLine(Solve());
        }
    }

    private static string Solve()
    {
        int[] counts = new int[8];
        bool bishopFound = false;
        string previousCoords = "";
        string bishopCoords = "";

        for (int i = 0; i < 8; i++)
        {
            string line = Console.ReadLine();
            if (bishopFound)
                continue;

            string squareCoords = "";
            int occupiedSquares = 0;
            for (int j = 0; j < line.Length; j++)
            {
                if (line[j] == '#')
                {
                    occupiedSquares++;
                    squareCoords = string.Format("{0} {1}", i + 1, j + 1);
                }
            }
            counts[i] = occupiedSquares;

            if (i >= 2 && occupiedSquares == 2 && counts[i - 1] == 1 && counts[i - 2] == 2)
            {
                bishopCoords = previousCoords;
                bishopFound = true;
            }
            previousCoords = squareCoords;
        }

        return bishopCoords;
    }
}