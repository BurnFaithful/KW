package Week04;

class RedHeadDuck {
	int duckWidth;
	int duckHeight;
	
	public RedHeadDuck() { //������ ��ȣ�ȿ� �ƹ��͵� ���� ��츦 �⺻ �����ڶ�� ��.
		 duckWidth = 100;
		 duckHeight = 100;
	}
	public RedHeadDuck(int w, int h) {
		duckWidth = w;
		duckHeight = h;
	}
	public void duckInfo() {
		System.out.println("�����Ӹ� ������ ���α��̴� " + duckWidth);
		System.out.println("�����Ӹ� ������ ���α��̴� " + duckHeight);
	}	
}
public class A04_Constructor {
	public static void main(String[] args) {
		RedHeadDuck ��ģ���� = new RedHeadDuck();
		��ģ����.duckInfo();
		
		RedHeadDuck �������� = new RedHeadDuck(300,200);
		��������.duckInfo();
	}
}









