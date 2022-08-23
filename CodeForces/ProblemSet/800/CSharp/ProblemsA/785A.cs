using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        Console.WriteLine(Solve(t));
    }

    private static int Solve(int t)
    {
        var polyhedrons = new Dictionary<string, int>()
        {
            { "Tetrahedron", 4 },
            { "Cube", 6 },
            { "Octahedron", 8 },
            { "Dodecahedron", 12 },
            { "Icosahedron", 20 }
        };
        int sides = 0;

        for (int i = 0; i < t; i++)
        {
            string polyhedron = Console.ReadLine();
            sides += polyhedrons[polyhedron];
        }

        return sides;
    }
}