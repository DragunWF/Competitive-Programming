using System;

public class Program
{
    private static void Main()
    {
        string a = Console.ReadLine();
        string b = Console.ReadLine();
        Console.WriteLine(Solve(a, b));
    }

    private static string Solve(string a, string b)
    {
        string output = "";
        for (int i = 0; i < a.Length; i++)
        {
            bool isOne = int.Parse(a[i].ToString()) + int.Parse(b[i].ToString()) == 1;
            output += isOne ? "1" : "0";
        }
        return output;
    }
}