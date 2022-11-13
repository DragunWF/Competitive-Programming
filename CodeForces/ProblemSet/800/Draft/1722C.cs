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
            Console.WriteLine(Solve(n));
        }
    }

    private static string Solve(int n)
    {
        int[] p = { 0, 0, 0 };
        string[][] arr = {
            Console.ReadLine().Split(' '),
            Console.ReadLine().Split(' '),
            Console.ReadLine().Split(' ')
        };

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < arr.Length; j++)
            {
                int x = (j + 1) % 2, y = j != 2 ? 2 : (j + 2) % 2;
                if (arr[x].Contains(arr[j][i]) && arr[y].Contains(arr[j][i]))
                {
                    continue;
                }
                else if (arr[x].Contains(arr[j][i]) || arr[y].Contains(arr[j][i]))
                {
                    p[j]++;
                }
                else
                {
                    p[j] += 3;
                }
            }
        }

        return string.Format("{0} {1} {2}", p[0], p[1], p[2]);
    }
}
