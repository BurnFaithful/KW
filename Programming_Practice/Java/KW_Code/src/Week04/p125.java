package Week04;
import java.util.Scanner;
public class p125 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		//a -> 97  z -> 122
		System.out.print("���ĺ� �ѱ��ڸ� �־��ּ���>> ");
		String str = scan.next();  //�Ѵܾ�...
		char ch = str.charAt(0);
		
		for(int i = ch; i >=97; i--) {
			System.out.print((char)i);
		}
	}
}	











