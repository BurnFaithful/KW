package Week04;

import java.util.Scanner;

public class �ǿ���2018181325_88p {
	public static void main(String[] args) {
		// ���������� 2000
		// �Ƹ޸�ī�� 2500
		// īǪġ�� 3000
		// ī��� 3500
		Scanner scanner = new Scanner(System.in); // �Է¹ޱ� ���� ��ü ����
		
		System.out.print("Ŀ�� �ֹ��ϼ��� >> "); // Ŀ�� �ֹ��� �Է¹������ ������ ��¹�
		String coffee = scanner.next(); // �Է¹��� ����(Ŀ�� ����)�� coffee ������ ����
		int count = scanner.nextInt(); // �Է¹��� ����(Ŀ�� ����)�� count ������ ����
				
		// if ��
		if (coffee.equals("����������")) // coffee ���� "����������"�� ���� ��
		{		
			System.out.println(2000 * count + "���Դϴ�."); // ���������� ���� Ŀ�� ������ count�� ���Ͽ� ���
		}
		else if (coffee.equals("�Ƹ޸�ī��")) // coffee ���� "�Ƹ޸�ī��"�� ���� ��
		{
			System.out.println(2500 * count + "���Դϴ�."); // �Ƹ޸�ī�� ���� Ŀ�� ������ count�� ���Ͽ� ���
		}
		else if (coffee.equals("īǪġ��")) // coffee ���� "īǪġ��"�� ���� ��
		{		
			System.out.println(3000 * count + "���Դϴ�."); // īǪġ�� ���� Ŀ�� ������ count�� ���Ͽ� ���
		}
		else if (coffee.equals("ī���")) // coffee ���� "ī���"�� ���� ��
		{					
			System.out.println(3500 * count + "���Դϴ�."); // ī��� ���� Ŀ�� ������ count�� ���Ͽ� ���
		}
		
		// Switch��
		/*switch (coffee)
		{
		case "����������":
			System.out.println(2000 * count + "���Դϴ�.");
			break;
		case "�Ƹ޸�ī��":
			System.out.println(2500 * count + "���Դϴ�.");
			break;
		case "īǪġ��":
			System.out.println(3000 * count + "���Դϴ�.");
			break;
		case "ī���":
			System.out.println(3500 * count + "���Դϴ�.");
			break;
		}*/
		
		
		scanner.close(); // ��ü ����
	}
}
