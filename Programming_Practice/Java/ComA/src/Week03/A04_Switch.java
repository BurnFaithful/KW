package Week03;

import java.util.Scanner;

public class A04_Switch {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("������ ���� �����Դϱ�? ");
		
		String month = scanner.nextLine(); // Ű����κ��� ���ڿ� �Է��Լ� nextLine()
		
		
		switch (month) {
		case "������":
			System.out.println("���� �����ô� ��");
			break;
		case "ȭ����":
			System.out.println("ȭ���ϰ� ���ô� ��");
			break;
		case "������":
			System.out.println("���� ���������� ���ô� ��");
			break;
		case "�����":
			System.out.println("�񱸸ۿ� ���� ��ĥ ������ ���ô� ��");
			break;
		case "�ݿ���":
			System.out.println("���ϰ� ���ô� ��");
			break;
		case "�����":
			System.out.println("���� ������ ���ô� ��");
			break;
		default:
			System.out.println("������ ã�ư��鼭 ���ô� ��");
			break;
		}
		
		scanner.close();	
	}
}
