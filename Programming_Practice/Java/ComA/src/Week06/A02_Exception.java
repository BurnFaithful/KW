package Week06;

public class A02_Exception {
	
	public void Test() throws InterruptedException
	{
		System.out.println("시간 타이머를 작동합니다.");
		
		Thread.sleep(1000);
		
		System.out.println("다 끝났는지 확인.");
	}
	
	public static void main(String[] args) throws InterruptedException {
		
		A02_Exception ae = new A02_Exception();
		
		ae.Test();
	}
}
