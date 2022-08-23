using System;
using System.Collections;
using System.Collections.Generic;

public class Test
{
    public static void Main()
    {
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            string[] scores = Console.ReadLine().Split(' ');
            int a = int.Parse(scores[0].ToString());
            int b = int.Parse(scores[1].ToString());
            Console.WriteLine(a > b ? a : b);
        }
    }
}