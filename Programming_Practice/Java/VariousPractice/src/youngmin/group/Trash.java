package youngmin.group;
import java.util.Scanner;

public class Trash {
	
	public static void main(String[] args)
	{
		// String
		// Integer == int
		// Double == double
		// Byte == byte
		// Object == 
		// . . . .
		
		// VB
		// Dim num As Integer
		// num = 10
		
		// Java
		// int, double, float, byte, boolean, char, String, Object, ...
		Scanner scanner = new Scanner(System.in);
		System.out.print("�г�> ");
		int A = scanner.nextInt();
		System.out.print("��> ");
		String B = scanner.next();
		System.out.print("����> ");
		float C = scanner.nextFloat();
		System.out.print("����> ");
		double D = scanner.nextDouble();
		
		scanner.close();
		System.out.println("�г� : " + A);
		System.out.println("�� : " + B);
		System.out.println("���� : " + C);
		System.out.println("���� : " + D);
	}
}
