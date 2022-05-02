using System;
using System.Collections.Generic;

public static class Kata
{
    public static long rowSumOddNumbers(long n)
    {
        var expectedListSize = 0;
        for (var i = 1; i <= n; i++)
            expectedListSize += i;

        var oddNumbers = new List<int>();
        var iterator = 0;
        while (oddNumbers.Count < expectedListSize)
        {
            iterator++;
            if (iterator % 2 != 0)
                oddNumbers.Add(iterator);
        }

        var sum = 0;
        for (var i = oddNumbers.Count - (int)n; i < oddNumbers.Count; i++)
            sum += oddNumbers[i];

        return Convert.ToInt64(sum);
    }
}

// Turns out everything could have been solved by doing n * n * n
// But I guess that serves as a lesson to not overthink things...