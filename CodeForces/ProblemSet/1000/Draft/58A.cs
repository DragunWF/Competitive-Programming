using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class CodeForces
{
    private static void Main()
    {
        string s = Console.ReadLine();
        Console.WriteLine(Solve(s));
    }

    private static string Solve(string s)
    {
        var charArr = s.ToCharArray();
        var charsSet = new HashSet<char>(charArr).ToArray();
        var charsPassed = new List<char>();

        if (charArr.Where(x => x != 'l').Count() <= 1)
            return "NO";

        int indexH = Array.IndexOf(charsSet, 'h');
        if (indexH == -1 || indexH + 3 >= charsSet.Length)
            return "NO";

        string joinedChars = string.Join("", charsSet);
        if (joinedChars.Substring(indexH, indexH + 3) != "helo")
            return "NO";

        return "YES";
    }
}