package Week03;

class �κ�Ʈ {
	public void ����() {
		System.out.println("�߷� ����.");
	}
	public void ����() {
		System.out.println("������� ����.");
	}
}
class �ٰ� extends �κ�Ʈ {
	
}
class �������̰� extends �κ�Ʈ {
	@Override
	public void ����() {
		System.out.println("���� �ظ�");
	}
}

public class A07_Class {
	public static void main(String[] args) {
		�ٰ� dg = new �ٰ�();
		dg.����();
		dg.����();
		
		�������̰� g = new �������̰�();
		g.����();
		g.����();
	}
}
