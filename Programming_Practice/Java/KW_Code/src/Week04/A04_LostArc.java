package Week04;

import java.util.Scanner;

class ���ӳ� {
	String name;
	String hairColor = "�Ͼ��";
	String skinColor = "�Ͼ��";
	int level = 1;
	
	public void ���ӳʻ����� () {
		System.out.println("������ ���ӳ� ĳ���̸�: " + name);
		System.out.println("���Į��:" + hairColor + ",�Ǻλ�:" + skinColor + ",���緹��:" + level);
	}
}
public class A04_LostArc {
	public static void main(String[] args) { //Ŭ�������� �̿��ؼ� ���� ���� ���α׷� �����ڵ��ϴ°�
		Scanner scan = new Scanner(System.in);
		
		���ӳ� s1 = null;
		boolean  flag = true;
		while(flag) {		
			System.out.println("1. ���ӳ� �ʱ����");
			System.out.println("2. ���ӳ� �󼼻���");
			System.out.println("3. ĳ���� ������ ���ӽ���");
			System.out.print(">> ");
			int menu = scan.nextInt();
			scan.nextLine();
			
			switch (menu) {
			case 1:
				if ( s1 == null ) {
					s1 = new ���ӳ�();
					System.out.print("������ �̸��� �Է��ϼ���>> ");
					s1.name = scan.nextLine();
					System.out.println("�ʱ� " + s1.name + " ���ӳ� ������!!");
				}else {
					System.out.println("�̹� ���ӳ� ��ü�� �����Ǿ���. �������Է�");
				}
				break;
			case 2:
				if ( s1 != null) {
					System.out.print("���ӳ��� �Ӹ� ���� �Է��Ͻÿ�>> ");				
					s1.hairColor = scan.nextLine();
					System.out.print("���ӳ��� �Ǻ� ���� �Է��Ͻÿ�>> ");
					s1.skinColor = scan.nextLine();
					s1.level = 10;
					s1.���ӳʻ�����();
				}else {
					System.out.println("���ӳ� �ʱ� �������� �ϼ���");
				}
				break;
			case 3:	
				if ( s1 == null ) {
					System.out.println("ĳ���� ���� �����ϼ���~");
				}else {
					flag = false;					
				}
				break;
			}
		}
		System.out.println("���� ���ӳʷ� ������ �����մϴ�.");
		
		scan.close();
	}
}






















