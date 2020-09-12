package youngmin.group;
import java.util.Scanner;

public class input {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.print("실수값을 입력하세요>> ");
		double input = scan.nextDouble();
		System.out.println(input);
		
		scan.close();
	}
}
