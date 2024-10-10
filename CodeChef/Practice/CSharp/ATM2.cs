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
		    int[] values = intArr();
		    int n = values[0];
		    int k = values[1];
		    int[] arr = intArr();
		    Console.WriteLine(Solve(n, k, arr));
		}
	}
	
	private static int[] intArr() 
	{ 
	    return Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
	}
	
	private static string Solve(int n, int k, int[] arr) 
	{ 
	    char[] output = new char[n];
	    for (int i = 0; i < n; i++)
	    {
	        if (k >= arr[i])
	        {
	            output[i] = '1';
	            k -= arr[i];
	        }
	        else
	            output[i] = '0';
	    }
	    return string.Join("", output);
	}
}
