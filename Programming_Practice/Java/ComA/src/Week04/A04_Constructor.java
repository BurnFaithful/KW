package Week04;

public class A04_Constructor {
	public static void main(String[] args) {
		RedHeadDuck crazyDuck = new RedHeadDuck();
		crazyDuck.DuckInfo();
		
		System.out.println("----------------------");
		
		RedHeadDuck userDuck = new RedHeadDuck(300, 200);
		userDuck.DuckInfo();
	}
}
