package Week06;

import java.util.Scanner;

public class A01_ExamMethod {
	
	static Scanner scan = new Scanner(System.in);
	
	public static void LinePrint()
	{
		System.out.println("==============================");
	}
	
	public static int myMax(int a, int b)
	{
		// �޼ҵ� �ȿ� �ִ� ���������� �ڵ��ʱ�ȭ�� ���� �ʴ´�.
		
/*		if (a > b)
			return a;
		else if (a == b)
			return a;
		else if (a < b)
			return b;
		else
			return 0;*/
		
		return a > b ? a : b;
	}
	
	public static boolean flgMax(int a, int b)
	{
		return a > b ? true : false;
	}
	
	public static boolean isPosNum(int num)
	{
		return num > 0 ? true : false;
	}
	
	// ���� ���ڰ� ���� ���ں��� ������ �ȵ�.
	public static int sum(int endNum, int firstNum)
	{
		int sum = 0;
		if (endNum > firstNum)
		{
			for (int i = firstNum; i <= endNum; i++)
			{
				sum += i;
			}
			return sum;
		}
		else return -1;
	}
	
	// ���� ���� �� ���� ����.
	public static int sumUpgrade(int num1, int num2)
	{
		int sum = 0;
		if (num1 <= num2)
		{
			for (int i = num1; i <= num2; i++)
				sum += i;
		}
		else
		{
			for (int i = num2; i <= num1; i++)
				sum += i;
		}
		
		return sum;
	}
	
	// �Է��� ���ڰ� ��������, ��������
	// A -> 65, Z -> 90
	// a -> 97, z -> 122
	public static boolean isAlphabet(char str)
	{
		if (str >= 65 && str <= 90 ||
				str >= 97 && str <= 122)
		{
			return true;
		}
		
		return false;
	}
	
	public static boolean isInteger(String str)
	{
		try
		{
			Integer.parseInt(str);
			return true;
		}
		catch (NumberFormatException e)
		{
			return false;
		}
	}
	
	public static void isInteger2()
	{
		while (true)
		{
			try
			{
				System.out.print("���� �Է� : ");
				int num = scan.nextInt();
			}
			catch (Exception e)
			{
				System.out.println("�߸� �Է��Ͽ����ϴ�.");
				scan.next();
				continue;
			}
			System.out.println("�����Դϴ�.");
			break;
		}
	}
	
	public static void main(String[] args) {
		
		int value = myMax(30, 40);
		boolean bool = flgMax(50, 30);
		boolean bool2 = isPosNum(-5);
		
		int sum = sum(10, 1);
		int sum2 = sumUpgrade(10, 1);
		
		System.out.println(value);
		System.out.println(bool);
		System.out.println(bool2);
		
		LinePrint();
		
		System.out.println("�� : " + sum);
		System.out.println("��2 : " + sum2);
		
		LinePrint();
		
		System.out.println("a : " + isAlphabet('a'));
		System.out.println("A : " + isAlphabet('A'));
		System.out.println("c : " + isAlphabet('c'));
		System.out.println("H : " + isAlphabet('H'));
		System.out.println("z : " + isAlphabet('z'));
		System.out.println("! : " + isAlphabet('!'));
		
		LinePrint();
		
		System.out.println("a : " + isInteger("a"));
		System.out.println("5 : " + isInteger("5"));
		System.out.println("10 : " + isInteger("10"));
		
		LinePrint();
		
		isInteger2();
	}
}
