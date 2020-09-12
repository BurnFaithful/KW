package Week12;

import java.util.Scanner;

public class A01_Exception {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int num1, num2;
		System.out.print("First Integer : ");
		num1 = scan.nextInt();
		System.out.print("Second Integer: ");
		num2 = scan.nextInt();
		
		int result = 0;
		
		try
		{
			result = num1 / num2;
		}
		catch (ArithmeticException e)
		{
			e.printStackTrace();
			System.err.println("0으로 나눌 수 없음.");
		}
		finally
		{
			System.out.println(num1 + " / " + num2 + " = " + result);
		}
			
		scan.close();
	}
}
