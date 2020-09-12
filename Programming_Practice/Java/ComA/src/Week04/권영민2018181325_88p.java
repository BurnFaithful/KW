package Week04;

import java.util.Scanner;

public class 권영민2018181325_88p {
	public static void main(String[] args) {
		// 에스프레소 2000
		// 아메리카노 2500
		// 카푸치노 3000
		// 카페라떼 3500
		Scanner scanner = new Scanner(System.in); // 입력받기 위한 객체 생성
		
		System.out.print("커피 주문하세요 >> "); // 커피 주문을 입력받으라는 헬프용 출력문
		String coffee = scanner.next(); // 입력받은 문자(커피 종류)를 coffee 변수에 대입
		int count = scanner.nextInt(); // 입력받은 숫자(커피 갯수)를 count 변수에 대입
				
		// if 문
		if (coffee.equals("에스프레소")) // coffee 값이 "에스프레소"와 같을 때
		{		
			System.out.println(2000 * count + "원입니다."); // 에스프레소 값에 커피 갯수값 count를 곱하여 출력
		}
		else if (coffee.equals("아메리카노")) // coffee 값이 "아메리카노"와 같을 때
		{
			System.out.println(2500 * count + "원입니다."); // 아메리카노 값에 커피 갯수값 count를 곱하여 출력
		}
		else if (coffee.equals("카푸치노")) // coffee 값이 "카푸치노"와 같을 때
		{		
			System.out.println(3000 * count + "원입니다."); // 카푸치노 값에 커피 갯수값 count를 곱하여 출력
		}
		else if (coffee.equals("카페라떼")) // coffee 값이 "카페라떼"와 같을 때
		{					
			System.out.println(3500 * count + "원입니다."); // 카페라떼 값에 커피 갯수값 count를 곱하여 출력
		}
		
		// Switch문
		/*switch (coffee)
		{
		case "에스프레소":
			System.out.println(2000 * count + "원입니다.");
			break;
		case "아메리카노":
			System.out.println(2500 * count + "원입니다.");
			break;
		case "카푸치노":
			System.out.println(3000 * count + "원입니다.");
			break;
		case "카페라떼":
			System.out.println(3500 * count + "원입니다.");
			break;
		}*/
		
		
		scanner.close(); // 객체 닫음
	}
}
