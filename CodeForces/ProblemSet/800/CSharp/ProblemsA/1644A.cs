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

    private static string Solve(string hallway)
    {
        var keys = new List<string>();
        foreach (char tile in hallway)
        {
            string tileString = tile.ToString();
            string key = tileString.ToLower();
            if (tileString == key)
                keys.Add(key);
            else if (!keys.Contains(key))
                return "NO";
        }
        return "YES";
    }
}