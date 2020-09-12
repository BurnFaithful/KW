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
				System.out.println("프로그램 종료!!!!");
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
		System.out.println("#### 로또 발생 가능 수 #####");
		for(int k = 0; k < rotto.length-1; k++) {
			System.out.print(rotto[k] + ",");			
		}		
		System.out.println("\n");
	}
	private static void allPrint(double result, int num) {
		result = Math.round(result * 100) / 100.0;	
		
		if( num == 1) {					
			System.out.println("###### 원의 넓이 결과 ######");		
			System.out.println("# 원넓이: " + result + " #\n");
		}else if (num == 2) {
			System.out.println("###### 사각형의 넓이 결과 ######");		
			System.out.println("# 사각형 넓이: " + result + " #\n");
		}else if (num == 3) {
			System.out.println("###### 삼각형의 넓이 결과 ######");
			System.out.println("# 삼각형 넓이: " + result + " #\n");
		}
	}
	
	
	private static void rectanglePrint(double result) {
		result = Math.round(result*100)/100.0;			
		System.out.println("###### 사각형의 넓이 결과 ######");		
		System.out.println("# 사각형 넓이: " + result + " #\n");		
	}
	private static double rectangleCalc() {				
		System.out.print("<<사각형 높이>> ");
		int height = scan.nextInt();
		System.out.print("<<사각형 밑변>> ");
		int under = scan.nextInt();		
		return height * under;
	}
	
	private static void trainglePrint(double result) {
		result = Math.round(result * 100) / 100.0;
		System.out.println("###### 삼각형의 넓이 결과 ######");
		System.out.println("# 삼각형 넓이: " + result + " #\n");		
	}
	private static double triangleCalc() {
		System.out.print("<<삼각형 높이>> ");
		int height = scan.nextInt();
		System.out.print("<<삼각형 밑변>> ");
		int under = scan.nextInt();		
		return (height * under) / 2;
	}
	private static int menudisplay() {
		System.out.println("1.원의 넓이를 구하라.");
		System.out.println("2.삼각형 넓이를 구하라.");
		System.out.println("3.사각형 넓이를 구하라.");
		System.out.println("4.로또 값 구하라.");
		System.out.println("5.끝내기.");
		System.out.print(">> ");
		
		return scan.nextInt();
	}
	private static void circlePrint(double circle) {		
		circle = Math.round(circle*100)/100.0;			
		System.out.println("###### 원의 넓이 결과 ######");		
		System.out.println("# 원넓이: " + circle + " #\n");		
	}
	private static double circleCalc() {
		System.out.print("\n<<원의 반지름>> ");
		int radius = scan.nextInt();	
		return Math.pow(radius, 2) * Math.PI;	
	}
}