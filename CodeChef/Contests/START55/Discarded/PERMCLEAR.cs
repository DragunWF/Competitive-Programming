using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public sealed class Test
{
	public static void Main()
	{
		int t = int.Parse(Console.ReadLine());
		for (int i = 0; i < t; i++) 
		{
		    Console.ReadLine();
		    string[] a = Console.ReadLine().Split(' ');
		    Console.ReadLine();
		    string[] b = Console.ReadLine().Split(' ');
		    string[] c = a.Where(x => !b.Contains(x)).ToArray();
		    Console.WriteLine(string.Join(' ', c));
		}
	}
}