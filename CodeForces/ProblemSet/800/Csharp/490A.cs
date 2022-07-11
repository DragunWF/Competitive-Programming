using System;
using System.Collections;
using System.Collections.Generic;

public class CodeForces
{
    private static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] students = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray();
        Solve(n, students); 
    }

    private static int MinimumLength(int[] arrayOfLengths)
    {
        int minimum = arrayOfLengths[0];
        for (int i = 1; i < arrayOfLengths.Length; i++)
            if (arrayOfLengths[i] < minimum)
                minimum = arrayOfLengths[i];
        return minimum;
    }

    private static void Solve(int n, int[] students)
    {
        var programmingStudents = new List<int>();
        var mathStudents = new List<int>();
        var peStudents = new List<int>();

        for (int i = 0; i < n; i++)
        {
            int index = i + 1;
            switch (students[i])
            {
                case 1:
                    programmingStudents.Add(index);
                    break;
                case 2:
                    mathStudents.Add(index);
                    break;
                case 3:
                    peStudents.Add(index);
                    break;
            }
        }

        var teams = new List<string>();
        int iterationCount = MinimumLength(new int[3] {
            programmingStudents.Count,
            mathStudents.Count,
            peStudents.Count
        });

        for (int i = 0; i < iterationCount; i++)
        {
            string team = string.Format("{0} {1} {2}", 
                programmingStudents[i], 
                mathStudents[i], 
                peStudents[i]
            );
            teams.Add(team);
        }

        Console.WriteLine(teams.Count);
        foreach (string team in teams)
            Console.WriteLine(team);
    }
}