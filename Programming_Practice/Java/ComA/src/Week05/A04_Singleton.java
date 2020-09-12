package Week05;

class Computer {
	
	static Computer com = new Computer();
	
	private Computer() {
		// TODO Auto-generated constructor stub
		System.out.println("컴퓨터 객체 생성");
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
