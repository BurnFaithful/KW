package Week03;

public class A03_While {
	public static void main(String[] args) {
		
		int i = 1;
		int oddSum = 0, evenSum = 0;
		while (i <= 100) {
			
			if (i % 2 != 0) 
			{
				//System.out.println(i);
				oddSum += i;
			}
			else evenSum += i;
			i++;
		}
		System.out.println(oddSum);
		System.out.println(evenSum);
	}
}
