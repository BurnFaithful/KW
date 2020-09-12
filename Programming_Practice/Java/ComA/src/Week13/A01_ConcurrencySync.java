package Week13;

class BankAccount
{
	private int balance = 50000;
	
	public int getBalance() { return balance; }
	
	public void withdraw(int amount) { this.balance = this.balance - amount; }
}

class RyanAndMonica implements Runnable
{
	BankAccount account = new BankAccount();
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		for (int i = 1; i <= 50; i++)
		{
			makeWithdrawal(1000);
			
			if (account.getBalance() < 0)
				System.out.println("잔고가 부족합니다.");
		}
	}
	
	public void makeWithdrawal(int amount)
	{
		if (account.getBalance() >= amount)
		{
			System.out.println(Thread.currentThread().getName() + "가 " + amount + "원을 인출합니다.");
			
			
			account.withdraw(amount);
			
			System.out.println("남은 잔고 : " + account.getBalance());
		}
		else
		{
			System.out.println(Thread.currentThread().getName() + "가 인출에 실패했습니다. 잔고가 부족합니다.");
		}
	}
	
}

public class A01_ConcurrencySync {
	public static void main(String[] args) {
		
		RyanAndMonica job = new RyanAndMonica();
		
		Thread ryan = new Thread(job);
		Thread monica = new Thread(job);
		
		ryan.setName("Ryan");
		monica.setName("Monica");
		
		ryan.start();
		monica.start();
	}
}
