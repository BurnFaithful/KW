package Week05;

import java.util.Scanner;

class ��ī�� {
	public String skinColor;
	public int level;
	
	//������ -> Ŭ���� �̸��� ������,  ���������� �ƿ�����,  �Ű������� 0�� �̻�, �������� ������ ������.
	public ��ī��() {		
		this.skinColor = "�����";
		this.level = 1;		
		System.out.println("��ī�� ����: " + skinColor);
		System.out.println("��ī�� ����: " + level);
	}
	public ��ī��(String skinColor, int level) { //������ �����ε�(�����ε�)
		this.skinColor = skinColor;
		this.level = level;
		System.out.println("��ī�� ����: " + skinColor);
		System.out.println("��ī�� ����: " + level);
	}
}
public class A01_PocketMongo {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("======== ��Ĺ��� ���� ========");
		System.out.println("1. �⺻ ��ī�� ����");
		System.out.println("2. ����� ���� ��ī�� ����");
		System.out.print("����(����3��)>> ");
		int cho = scan.nextInt();
		
		switch (cho) {
		case 1: 
			System.out.println("��ī�� ���ϸ��Ͱ� �⺻���� �����Ǿ���!!!");
			new ��ī��();  
			break;
		case 2:
			System.out.println("����ڰ� ���� �������ϴ� ��ī�� ���ϸ��� ����!!!");
			System.out.print("�⺻ �Ǻλ���? ");
			String skinColor = scan.next();
			System.out.print("���ϸ��� �⺻������? ");
			int level = scan.nextInt();					
			new ��ī��(skinColor, level);			
			break;
		default:
			System.out.println("���� ����!!!");
			System.exit(1); //���α׷� ���� ����.
			break;
		}
		
		scan.close();
	}
}



















