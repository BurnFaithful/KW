package Week06;

public class Z02_Exception {
	
	public void Test() throws InterruptedException {
		System.out.println("�ð� Ÿ�̸Ӹ� �۵��մϴ�.~~~");
		
		Thread.sleep(5000);
		
		System.out.println("�� ������?");
	}	
	public static void main(String[] args) throws InterruptedException {
		Z02_Exception ze = new Z02_Exception();
		
		ze.Test();
	}
}
