package youngmin.sort;

import java.util.ArrayList;
import java.util.Arrays;

import youngmin.util.UtilityMethod;

public class BubbleSort {

	private static ArrayList<Integer> noneSortArr;
	
	public BubbleSort()
	{
		noneSortArr = new ArrayList<Integer>();
	}
	
	
	public static void setArray(int... x)
	{
		
	}
	
	
	public static void sort()
	{
		for (int i = 0; i < noneSortArr.size(); i++)
		{
			for (int j = i + 1; j < noneSortArr.size(); j++)
			{
				if (noneSortArr.get(i) > noneSortArr.get(j))
				{
					UtilityMethod.swap(noneSortArr, i, j);
				}
			}
		}
		
		for (int i = 0; i < noneSortArr.size(); i++)
			System.out.print(noneSortArr.get(i) + " ");
	}
	
	public static void sort(ArrayList<Integer> arr)
	{
		for (int i = 0; i < arr.size(); i++)
		{
			for (int j = i + 1; j < arr.size(); j++)
			{
				if (arr.get(i) > arr.get(j))
				{
					UtilityMethod.swap(arr, i, j);
				}
			}
		}
		
		for (int i = 0; i < arr.size(); i++)
			System.out.print(arr.get(i) + " ");
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> arrList = new ArrayList<Integer>(Arrays.asList(10, 2, 6, 8, 3, 13));

		BubbleSort.sort(arrList);
	}
}
