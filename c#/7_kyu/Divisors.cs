// https://www.codewars.com/kata/544aed4c4a30184e960010f4

using System.Collections.Generic;

public class Kata
{
    public static int[] Divisors(int n)
    {
        List<int> divisors = new List<int>();
        for (int i = 2; i < n; i++)
        {
            if (n % i == 0)
            {
                divisors.Add(i);
            }
        }
        return divisors.Count >= 1 ? divisors.ToArray() : null;
    }
}