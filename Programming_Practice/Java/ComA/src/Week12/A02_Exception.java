package Week12;

import java.util.Scanner;

// ���� ���� ȸ���� ���� ����ó��
public class A02_Exception {

	@SuppressWarnings("resource")
	public static void main(String[] args) throws DanceException {
		
		Scanner scan = new Scanner(System.in);
		
		int women = 0, men = 0;
		
		System.out.print("�����п� ���� ȸ�� �� �Է� : ");
		women = scan.nextInt();
		
		System.out.print("�����п� ���� ȸ�� �� �Է� : ");
		men = scan.nextInt();
		
		if (women == 0)
		{
			throw new DanceException("���� ȸ������ �����ϴ�.");
		}
		else if (men == 0)
		{
			throw new DanceException("���� ȸ������ �����ϴ�.");
		}
		else
			System.out.println("���� ���Ǹ� �����մϴ�.");
		
		scan.close();
	}
}