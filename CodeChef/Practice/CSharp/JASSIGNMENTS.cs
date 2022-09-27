using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class Test
{
	public static void Main()
	{
		int t = int.Parse(Console.ReadLine());
		for (int i = 0; i < t; i++) 
		{ 
		    int x = int.Parse(Console.ReadLine());
		    Console.WriteLine(Solve(x));
		}
	}
	
	private static string Solve(int x) 
	{ 
	    return 10 - x >= 3 ? "YES" : "NO";
	}
}