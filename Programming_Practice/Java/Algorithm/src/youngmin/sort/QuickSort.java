package youngmin.sort;

import youngmin.util.*;

public class QuickSort {

	private static int order = 0;
	
	// 리스트 내에서 피벗(Pivot)을 결정
	// 피벗을 기준으로 왼쪽 포인트(Left)와 오른쪽 포인트(Right)를 통해 비교
	// 피벗 왼쪽엔 피벗보다 작은 값, 피벗 오른쪽엔 피벗보다 작은 값이 있도록
	// Left는 우측으로, Right는 좌측으로 이동하면서 값 비교를 수행하고 위 조건에 해당하면 Swap 수행
	// 조건에 해당하지 않는다면 피벗과 Swap
	// 피벗과 Swap을 했다면 해당 피벗을 기준으로 위 과정을 정렬이 끝날 때까지 재수행
	
	public void sort(int[] arr, int begin, int end)
	{
		if (begin < end)
		{
			int p = partition(arr, begin, end);
			sort(arr, begin, p - 1);
			sort(arr, p + 1, end);
		}
	}
	
	public int partition(int[] arr, int begin, int end)
	{
		int left = begin;
		int right = end;
		
		int pivot = (left + right) / 2; // 중위점을 피벗으로 설정
		
		order++;
		System.out.println("퀵 정렬 " + order + " 단계, Pivot : " + arr[pivot]);
		
		while (left < right) // left와 right가 만나기 전까지 수행
		{
			while (arr[left] < arr[pivot] && left < right) // left가 피벗보다 큰 경우 hold
			{
				left++;
			}
			while (arr[right] > arr[pivot] && left < right) // right가 피벗보다 작은 경우 hold
			{
				right--;
			}
			
			if (left < right) // left, right가 만나기 전에 둘 다 hold할 경우 left, right를 swap
			{
				UtilityMethod.swap(arr, left, right);
				left++;
				right--;
			}
		}
		
		UtilityMethod.swap(arr, pivot, right); // left와 right가 만난다면 pivot과 right를 swap
		
		for (int i = 0; i < arr.length; i++)
		{
			System.out.print(arr[i] + " ");
		}
		System.out.println();
		
		return left;
	}
	
	public static void main(String[] args) {
		QuickSort sorter = new QuickSort();
		
		int[] testArr = { 10, 17, 5, 3, 16, 39, 27, 41, 52, 7 };
		
		sorter.sort(testArr, 0, testArr.length - 1);
	}
}
