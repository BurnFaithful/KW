package Week06;
import java.util.Scanner;
public class Z02_Mehod {		
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("ù��° ���� ���� ���Է�>> ");
		int start = scan.nextInt();
		System.out.print("������ ���� ���Է�>> ");
		int end = scan.nextInt();
		
		guguTable(start, end);		
		scan.close();
	}
	private static void guguTable(int start, int end) {		
		int i, j;		
		for(i = 1; i <= 9; i++) {
			for(j = start; j <= end; j++) {
				System.out.printf("%d*%d=%2d  ", j, i, i*j);
			}
			System.out.println();
		}
	}	
}















