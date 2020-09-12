package Week06;

public class Z02_Exception {
	
	public void Test() throws InterruptedException {
		System.out.println("시간 타이머를 작동합니다.~~~");
		
		Thread.sleep(5000);
		
		System.out.println("다 끝났나?");
	}	
	public static void main(String[] args) throws InterruptedException {
		Z02_Exception ze = new Z02_Exception();
		
		ze.Test();
	}
}
