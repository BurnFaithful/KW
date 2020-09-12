package Week12;

class Essen extends Thread
{
	int number;
	
	public Essen() {
	
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

public class A05_Thread {

	public static void main(String[] args) {
		
		Essen thread1 = new Essen();
		Essen thread2 = new Essen();
		thread1.start();
		thread2.start();
	}
}
