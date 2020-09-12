package youngmin.sort;

import youngmin.util.*;

public class QuickSort {

	private static int order = 0;
	
	// ����Ʈ ������ �ǹ�(Pivot)�� ����
	// �ǹ��� �������� ���� ����Ʈ(Left)�� ������ ����Ʈ(Right)�� ���� ��
	// �ǹ� ���ʿ� �ǹ����� ���� ��, �ǹ� �����ʿ� �ǹ����� ���� ���� �ֵ���
	// Left�� ��������, Right�� �������� �̵��ϸ鼭 �� �񱳸� �����ϰ� �� ���ǿ� �ش��ϸ� Swap ����
	// ���ǿ� �ش����� �ʴ´ٸ� �ǹ��� Swap
	// �ǹ��� Swap�� �ߴٸ� �ش� �ǹ��� �������� �� ������ ������ ���� ������ �����
	
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
		
		int pivot = (left + right) / 2; // �������� �ǹ����� ����
		
		order++;
		System.out.println("�� ���� " + order + " �ܰ�, Pivot : " + arr[pivot]);
		
		while (left < right) // left�� right�� ������ ������ ����
		{
			while (arr[left] < arr[pivot] && left < right) // left�� �ǹ����� ū ��� hold
			{
				left++;
			}
			while (arr[right] > arr[pivot] && left < right) // right�� �ǹ����� ���� ��� hold
			{
				right--;
			}
			
			if (left < right) // left, right�� ������ ���� �� �� hold�� ��� left, right�� swap
			{
				UtilityMethod.swap(arr, left, right);
				left++;
				right--;
			}
		}
		
		UtilityMethod.swap(arr, pivot, right); // left�� right�� �����ٸ� pivot�� right�� swap
		
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
