package Week04;

public class RedHeadDuck {
	int duckWidth;
	int duckHeight;
	
	public RedHeadDuck()
	{
		duckWidth = 100;
		duckHeight = 100;
	}
	
	public RedHeadDuck(int w, int h)
	{
		duckWidth = w;
		duckHeight = h;
	}
	
	public void DuckInfo()
	{
		System.out.println("�����Ӹ� ������ ���α��� : " + duckWidth);
		System.out.println("�����Ӹ� ������ ���α��� : " + duckHeight);
	}
}
