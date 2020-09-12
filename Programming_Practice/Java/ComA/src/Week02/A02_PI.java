package Week02;

import java.util.Scanner;

public class A02_PI {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.print("반지름 입력>> ");
		double radius = scan.nextDouble();
		
		double circle = radius * radius * 3.14159265;
		
		System.out.println("원의 넓이 = " + circle);
		
		scan.close();
}
}
