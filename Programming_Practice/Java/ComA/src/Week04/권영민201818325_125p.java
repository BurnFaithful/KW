package Week04;

import java.util.Scanner;

public class �ǿ���201818325_125p {
	public static void main(String[] args) {
		// ���� �ҹ��ڸ� �ϳ� �Է¹ް� �� ���ں��� ���ĺ� ������ ����
		// ��� ���ڸ� ����ϴ� ���α׷�
		// a -> 97, Z -> 122
		
		Scanner scanner = new Scanner(System.in); // �Է� ��ü ����
		System.out.print("���ĺ� �� ���ڸ� �Է��ϼ��� >> "); // ���ĺ� ���ڸ� �Է��϶�� ���� ��¹�
		
		String alphabet = scanner.next(); // ���ĺ� ���� �Է¹���
		char c = alphabet.charAt(0); // �Է¹��� ���ڿ����� ���� �ϳ��� �޾� char ���� c�� ����
		
		for (int i = 97; i <= c; i++) // a ~ c�� ������ for�� �ݺ�
		{
			for (int j = i; j <= c; j++) // ���κ� ���� ���ĺ��� �ϳ��� �÷����� ���� for��(ù° ���� a����, ��° ���� b����, ...)
			{
				System.out.print((char)j); // a ~ c�� ������ ���
			}
			System.out.println(); // �� ���� ����� ������ ����.
		}
		
		scanner.close(); // �Է� ��ü ����� ���� �� ����.
	}
}
