package Week03;

import java.util.Scanner;

public class A04_Switch {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("오늘은 무슨 요일입니까? ");
		
		String month = scanner.nextLine(); // 키보드로부터 문자열 입력함수 nextLine()
		
		
		switch (month) {
		case "월요일":
			System.out.println("원래 술마시는 날");
			break;
		case "화요일":
			System.out.println("화끈하게 마시는 날");
			break;
		case "수요일":
			System.out.println("숨이 막힐때까지 마시는 날");
			break;
		case "목요일":
			System.out.println("목구멍에 술이 넘칠 때까지 마시는 날");
			break;
		case "금요일":
			System.out.println("급하게 마시는 날");
			break;
		case "토요일":
			System.out.println("토할 때까지 마시는 날");
			break;
		default:
			System.out.println("일일이 찾아가면서 마시는 날");
			break;
		}
		
		scanner.close();	
	}
}
