package Week13;

class Buffer
{
	private int data;
	private boolean empty = true;
	
	public synchronized int get()
	{
		while (empty)
		{
			try
			{
				wait();
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
		empty = true;
		notifyAll();
		System.out.println("�Һ���: " + this.data + "��° �ɟ��� �Һ���.");
		return data;
	}
	
	public synchronized void put(int data)
	{
		while (!empty)
		{
			try
			{
				wait();
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
		empty = false;
		this.data = data;
		System.out.println("������: " + this.data + "��° �ɟ��� ������.");
		notifyAll();
	}
}

class Producer implements Runnable
{
	private Buffer buffer;

	public Producer(Buffer buffer)
	{
		this.buffer = buffer;
	}
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for (int i = 1; i <= 10; i++)
		{
			buffer.put(i);
			
			try
			{
				Thread.sleep((int)Math.random() * 1000);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
	}
}

class Consumer implements Runnable
{
	private Buffer buffer;
	
	public Consumer(Buffer buffer)
	{
		this.buffer = buffer;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		for (int i = 1; i <= 10; i++)
		{
			buffer.get();
			
			try
			{
				Thread.sleep((int) Math.random() * 1000);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
	}
	
	
}

public class A02_ProducerAndConsumer {

	public static void main(String[] args) {
		
		Buffer buffer = new Buffer();
		Producer producer = new Producer(buffer);
		Consumer consumer = new Consumer(buffer);
		
		Thread producerThread = new Thread(producer);
		Thread consumerThread = new Thread(consumer);
		
		producerThread.start();
		consumerThread.start();
	}
}
