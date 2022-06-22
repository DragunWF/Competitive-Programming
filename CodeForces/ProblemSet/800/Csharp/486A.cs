using System;

public class Program
{
    private static void Main()
    {
        long n = Convert.ToInt64(Console.ReadLine());
        Console.WriteLine(Solve(n));
    }

    private static long Solve(long n)
    {
        long r = n / 2;
        return n % 2 == 0 ? r : -r - 1;
    }
}