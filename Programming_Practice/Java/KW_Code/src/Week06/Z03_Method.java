package Week06;
import java.util.Scanner;
public class Z03_Method {
	static Scanner scan = new Scanner(System.in);
	
	public static void main(String[] args) {				
		int key;
		double result;
		
		while(true) {
			key = menudisplay();			
			
			switch (key) {
			case 1:							
				result = circleCalc();		
				//circlePrint(result);
				allPrint(result, 1);
				break;
			case 2:
				result = triangleCalc();
				//trainglePrint(result);
				allPrint(result, 2);
				break;
			case 3:
				result = rectangleCalc();				
				//rectanglePrint(result);
				allPrint(result, 3);
				break;
			case 4:
				rottoFunc();
				break;
			case 5:
				System.out.println("���α׷� ����!!!!");
				System.exit(1);
			default:
				break;
			}
		}		
	}	
	private static void rottoFunc() {
		int[] rotto = new int[7];	
		
		for(int i = 1; i < rotto.length; i++) {			
			rotto[i] = (int)((Math.random() * 45) + 1 );
			
			for(int j = 0 ; j < i; j++ ) {
				if( rotto[j] == rotto[i]) {
					i--;
					break;
				}									
			}
		}
		System.out.println("#### �ζ� �߻� ���� �� #####");
		for(int k = 0; k < rotto.length-1; k++) {
			System.out.print(rotto[k] + ",");			
		}		
		System.out.println("\n");
	}
	private static void allPrint(double result, int num) {
		result = Math.round(result * 100) / 100.0;	
		
		if( num == 1) {					
			System.out.println("###### ���� ���� ��� ######");		
			System.out.println("# ������: " + result + " #\n");
		}else if (num == 2) {
			System.out.println("###### �簢���� ���� ��� ######");		
			System.out.println("# �簢�� ����: " + result + " #\n");
		}else if (num == 3) {
			System.out.println("###### �ﰢ���� ���� ��� ######");
			System.out.println("# �ﰢ�� ����: " + result + " #\n");
		}
	}
	
	
	private static void rectanglePrint(double result) {
		result = Math.round(result*100)/100.0;			
		System.out.println("###### �簢���� ���� ��� ######");		
		System.out.println("# �簢�� ����: " + result + " #\n");		
	}
	private static double rectangleCalc() {				
		System.out.print("<<�簢�� ����>> ");
		int height = scan.nextInt();
		System.out.print("<<�簢�� �غ�>> ");
		int under = scan.nextInt();		
		return height * under;
	}
	
	private static void trainglePrint(double result) {
		result = Math.round(result * 100) / 100.0;
		System.out.println("###### �ﰢ���� ���� ��� ######");
		System.out.println("# �ﰢ�� ����: " + result + " #\n");		
	}
	private static double triangleCalc() {
		System.out.print("<<�ﰢ�� ����>> ");
		int height = scan.nextInt();
		System.out.print("<<�ﰢ�� �غ�>> ");
		int under = scan.nextInt();		
		return (height * under) / 2;
	}
	private static int menudisplay() {
		System.out.println("1.���� ���̸� ���϶�.");
		System.out.println("2.�ﰢ�� ���̸� ���϶�.");
		System.out.println("3.�簢�� ���̸� ���϶�.");
		System.out.println("4.�ζ� �� ���϶�.");
		System.out.println("5.������.");
		System.out.print(">> ");
		
		return scan.nextInt();
	}
	private static void circlePrint(double circle) {		
		circle = Math.round(circle*100)/100.0;			
		System.out.println("###### ���� ���� ��� ######");		
		System.out.println("# ������: " + circle + " #\n");		
	}
	private static double circleCalc() {
		System.out.print("\n<<���� ������>> ");
		int radius = scan.nextInt();	
		return Math.pow(radius, 2) * Math.PI;	
	}
}