// https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/csharp

using System;

public class Kata
{
  public static int[] SortNumbers(int[] nums)
  {
    if (nums == null || nums.Length == 0)
      return new int[] { };
    Array.Sort(nums);
    return nums;
  }
}