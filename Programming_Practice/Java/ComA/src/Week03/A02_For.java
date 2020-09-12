package Week03;

public class A02_For {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 1; i <= 9; i++) 
		{
			for (int j = 2; j <= 9; j++) 
			{
				System.out.printf("%d * %d = %2d ", j, i, j * i);
			}
			System.out.println();
		}
	}
}
