package Week06;

public class A02_Exception {
	
	public void Test() throws InterruptedException
	{
		System.out.println("�ð� Ÿ�̸Ӹ� �۵��մϴ�.");
		
		Thread.sleep(1000);
		
		System.out.println("�� �������� Ȯ��.");
	}
	
	public static void main(String[] args) throws InterruptedException {
		
		A02_Exception ae = new A02_Exception();
		
		ae.Test();
	}
}
