package Week05;

class ��۱� {
	public static int KBS1 = 9, KBS2 = 7, SBS = 6, MBC = 11, JTBC = 15, EBS = 13;
}

public class A01_Static {
	public static void main(String[] args) {
		// �޸𸮴� ���� ����(Static), ���� ����(Heap), ���� ����
		// ���� ���� -> new�� ������ ��ü�� �����.
		// ���� ���� -> ������ ����, ���α׷� ���� ���� ���� �Ǵ� �޼ҵ尡 ����Ǵ� ��.
		//			���α׷� ���ᶧ���� �޸𸮿��� ������ ��.
		//			��ü ���α׷����� �� �� ���� ������.
		
		System.out.println("���ݺ��� ��۱� ä���� �ȳ��ϰڽ��ϴ�.");
		
		System.out.println("�ѱ������ " + ��۱�.KBS1 + ", " + ��۱�.KBS2 + " ä��!");
		System.out.println("��ȭ����� " + ��۱�.MBC + " ä��!");
		System.out.println("�������� " + ��۱�.SBS + " ä��!");
		System.out.println("��������� " + ��۱�.EBS + " ä��!");
		
		System.out.println("������ ���� �Ⱦ��!!!!");
		System.out.println(Math.abs(-3));
	}
}
