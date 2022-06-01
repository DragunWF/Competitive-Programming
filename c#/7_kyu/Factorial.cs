using System;

public static class Kata
{
    public static int Factorial(int n)
    {
        if (n < 0 || n > 12)
            throw new ArgumentOutOfRangeException();

        var output = 1;
        var multiplier = n;
        while (multiplier > 1)
        {
            output *= multiplier;
            multiplier--;
        }
        return output;
    }
}

// https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/csharp