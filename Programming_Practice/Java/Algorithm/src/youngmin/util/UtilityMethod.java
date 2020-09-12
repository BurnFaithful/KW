package youngmin.util;

import java.util.ArrayList;

public final class UtilityMethod {
	
	public static void swap(int[] arr, int x, int y)
	{
		int temp;
		
		temp = arr[x];
		arr[x] = arr[y];
		arr[y] = temp;
	}
	
	public static void swap(ArrayList<Integer> arrList, int x, int y)
	{
		int temp;
		
		temp = arrList.get(x);
		arrList.set(x, arrList.get(y));
		arrList.set(y, temp);
	}
}
