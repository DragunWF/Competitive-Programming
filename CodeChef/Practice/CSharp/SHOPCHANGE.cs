using System;

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
	
	private static int Solve(int x) 
	{ 
	    return 100 - x;
	}
}