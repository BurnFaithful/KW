package Week03;

import java.util.Scanner;

public class A06_BMI {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("너의 몸무게는? ");
		double weight = scanner.nextDouble();
		
		System.out.print("너의 키는? ");
		double height = scanner.nextDouble();
		height *= 0.01; // cm input
		
		double BMI = weight / (height * height);
		
		if (BMI < 18.5)
		{
			System.out.println("BMI : " + BMI + ", 저체중");
		}
		else if (BMI >= 18.5 && BMI <= 24.9)
		{
			System.out.println("BMI : " + BMI + ", 정상");
		}
		else if (BMI >= 25.0 && BMI <= 29.9)
		{
			System.out.println("BMI : " + BMI + ", 과체중");
		}
		else
		{
			System.out.println("BMI : " + BMI + ", 비만");
		}
		
		scanner.close();
	}
}
