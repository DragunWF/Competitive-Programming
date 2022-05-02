namespace Solution
{
  class Kata
    {
    public static int find_it(int[] seq) 
      {
        foreach (var n in seq)
          if (CountOccurences(seq, n) % 2 != 0)
            return n;
        return 0;
      }
    static int CountOccurences(int[] array, int element) 
      {
        var count = 0;
        foreach (var n in array)
          if (n == element)
            count++;
        return count;
      }
    }
}

// https://www.codewars.com/kata/54da5a58ea159efa38000836/train/csharp