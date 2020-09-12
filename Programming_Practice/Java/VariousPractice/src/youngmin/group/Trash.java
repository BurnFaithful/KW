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
		System.out.print("학년> ");
		int A = scanner.nextInt();
		System.out.print("반> ");
		String B = scanner.next();
		System.out.print("학점> ");
		float C = scanner.nextFloat();
		System.out.print("학점> ");
		double D = scanner.nextDouble();
		
		scanner.close();
		System.out.println("학년 : " + A);
		System.out.println("반 : " + B);
		System.out.println("학점 : " + C);
		System.out.println("학점 : " + D);
	}
}
