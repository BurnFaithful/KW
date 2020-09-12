package Week02;

import java.util.Scanner;

public class A01_Input {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello Java~!");
		//System.out.println("Hello Java~!");
		
		// 키보드로부터 입력
		Scanner scan = new Scanner(System.in);
		
		System.out.print("자주하는 게임 이름? ");
		String game = scan.nextLine();
		System.out.println("게임 이름 >> " + game);
		
		System.out.print("너 몇살이야? ");
		int age = scan.nextInt();
		System.out.println(age);
		
		scan.close();
	}

}
