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
		System.out.println("붉은머리 오리의 가로길이 : " + duckWidth);
		System.out.println("붉은머리 오리의 세로길이 : " + duckHeight);
	}
}
