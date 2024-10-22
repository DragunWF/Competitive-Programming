// https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/csharp

public static class Kata
{
    public static int[] Incrementer(int[] numbers)
    {
        int[] result = new int[numbers.Length];
        for (int i = 0, pos = 1; i < result.Length; i++, pos++)
        {
            int sum = numbers[i] + pos;
            if (sum >= 10)
            {
                sum %= 10;
            }
            result[i] = sum;
        }
        return result;
    }
}