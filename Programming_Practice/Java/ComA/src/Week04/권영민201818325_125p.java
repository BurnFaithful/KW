package Week04;

import java.util.Scanner;

public class 권영민201818325_125p {
	public static void main(String[] args) {
		// 영문 소문자를 하나 입력받고 그 문자보다 알파벳 순위가 낮은
		// 모든 문자를 출력하는 프로그램
		// a -> 97, Z -> 122
		
		Scanner scanner = new Scanner(System.in); // 입력 객체 생성
		System.out.print("알파벳 한 문자를 입력하세요 >> "); // 알파벳 문자를 입력하라는 헬프 출력문
		
		String alphabet = scanner.next(); // 알파벳 문자 입력받음
		char c = alphabet.charAt(0); // 입력받은 문자열에서 문자 하나만 받아 char 변수 c에 대입
		
		for (int i = 97; i <= c; i++) // a ~ c의 값까지 for문 반복
		{
			for (int j = i; j <= c; j++) // 라인별 시작 알파벳을 하나씩 늘려가기 위한 for문(첫째 줄은 a부터, 둘째 줄은 b부터, ...)
			{
				System.out.print((char)j); // a ~ c의 값까지 출력
			}
			System.out.println(); // 한 라인 출력이 끝나면 띄어쓰기.
		}
		
		scanner.close(); // 입력 객체 사용이 끝난 후 닫음.
	}
}
