package Week06;

import java.util.Scanner;

public class Z04_Method {
	public static void main(String[] args) {
						
			
		
	}
	private static void rectanglePrint(double result) {
		result = Math.round(result*100)/100.0;			
		System.out.println("###### �簢���� ���� ��� ######");		
		System.out.println("# �簢�� ����: " + result + " #\n");		
	}
	private static double rectangleCalc() {
		Scanner scan = new Scanner(System.in);		
		System.out.print("<<�簢�� ����>> ");
		int height = scan.nextInt();
		System.out.print("<<�簢�� �غ�>> ");
		int under = scan.nextInt();
		
		return height * under;
	}
}








