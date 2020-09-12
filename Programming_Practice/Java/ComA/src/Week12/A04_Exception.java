package Week12;

public class A04_Exception {
	
	public void go() throws InterruptedException
	{
		domore();
	}
	
	public void domore() throws InterruptedException
	{
		under();
	}
	
	public void under() throws InterruptedException
	{
		Thread.sleep(1000);
	}
	
	public static void main(String[] args) throws InterruptedException {
		
		A04_Exception ae = new A04_Exception();
		
		ae.go();
	}
}
