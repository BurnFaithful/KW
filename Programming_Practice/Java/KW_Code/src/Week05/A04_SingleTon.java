package Week05;

class ��ǻ�� {	
	static ��ǻ�� computer = null;
	
	private ��ǻ��() {
		if (computer == null) {
			computer = new ��ǻ��();
		}
		System.out.println("��ǻ�� ��ü ����");
	}
	public void ����̳��ض�() {
		System.out.println("������ ��ü�̴϶�~~~~~");
	}
}
public class A04_SingleTon {
	public static void main(String[] args) {
		��ǻ��.computer.����̳��ض�();
	}
}




