package Week02;

import java.util.Scanner;

public class A01_Input {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello Java~!");
		//System.out.println("Hello Java~!");
		
		// Ű����κ��� �Է�
		Scanner scan = new Scanner(System.in);
		
		System.out.print("�����ϴ� ���� �̸�? ");
		String game = scan.nextLine();
		System.out.println("���� �̸� >> " + game);
		
		System.out.print("�� ����̾�? ");
		int age = scan.nextInt();
		System.out.println(age);
		
		scan.close();
	}

}
