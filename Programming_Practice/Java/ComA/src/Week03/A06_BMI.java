package Week03;

import java.util.Scanner;

public class A06_BMI {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("���� �����Դ�? ");
		double weight = scanner.nextDouble();
		
		System.out.print("���� Ű��? ");
		double height = scanner.nextDouble();
		height *= 0.01; // cm input
		
		double BMI = weight / (height * height);
		
		if (BMI < 18.5)
		{
			System.out.println("BMI : " + BMI + ", ��ü��");
		}
		else if (BMI >= 18.5 && BMI <= 24.9)
		{
			System.out.println("BMI : " + BMI + ", ����");
		}
		else if (BMI >= 25.0 && BMI <= 29.9)
		{
			System.out.println("BMI : " + BMI + ", ��ü��");
		}
		else
		{
			System.out.println("BMI : " + BMI + ", ��");
		}
		
		scanner.close();
	}
}
