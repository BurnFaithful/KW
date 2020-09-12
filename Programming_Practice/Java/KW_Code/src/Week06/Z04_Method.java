package Week06;

import java.util.Scanner;

public class Z04_Method {
	public static void main(String[] args) {
						
			
		
	}
	private static void rectanglePrint(double result) {
		result = Math.round(result*100)/100.0;			
		System.out.println("###### 사각형의 넓이 결과 ######");		
		System.out.println("# 사각형 넓이: " + result + " #\n");		
	}
	private static double rectangleCalc() {
		Scanner scan = new Scanner(System.in);		
		System.out.print("<<사각형 높이>> ");
		int height = scan.nextInt();
		System.out.print("<<사각형 밑변>> ");
		int under = scan.nextInt();
		
		return height * under;
	}
}








