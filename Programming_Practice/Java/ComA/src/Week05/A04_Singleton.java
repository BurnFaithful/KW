package Week05;

class Computer {
	
	static Computer com = new Computer();
	
	private Computer() {
		// TODO Auto-generated constructor stub
		System.out.println("��ǻ�� ��ü ����");
	}
	
	public void Print()
	{
		System.out.println("Only one.");
	}
}

public class A04_Singleton {
	public static void main(String[] args) {
		Computer.com.Print();
	}
}
