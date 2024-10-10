// https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/csharp

using System;

public class Kata
{
    public static double SquareArea(double A)
    {
        return Math.Round((4 * Math.Pow(A, 2)) / Math.Pow(Math.PI, 2), 2);
    }
}