// https://www.codewars.com/kata/57a62154cf1fa5b25200031e/train/csharp

using System;
using System.Text;

namespace Solution
{
    public static class Program
    {
        public static string alternateCase(string s)
        {
            StringBuilder output = new StringBuilder();
            foreach (char c in s)
            {
                string str = c.ToString();
                output.Append(str == str.ToUpper() ? str.ToLower() : str.ToUpper());
            }
            return output.ToString();
        }
    }
}