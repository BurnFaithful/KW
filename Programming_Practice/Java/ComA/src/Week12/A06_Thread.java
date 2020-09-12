package Week12;

class JAVA implements Runnable
{
	int number;
	
	public JAVA() {
	
	}
	
	@Override
	public void run()
	{
		number = 1;
		while (true)
		{
			System.out.println(number + " : " + Thread.currentThread().getName());
			number++;
			
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}

public class A06_Thread {
	public static void main(String[] args) {
		
		Runnable rJob = new JAVA();
		
		Thread t1 = new Thread(rJob);
		Thread t2 = new Thread(rJob);
		Thread t3 = new Thread(rJob);
		
		t1.start();
		t2.start();
		t3.start();
	}
}
