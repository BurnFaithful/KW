package Week12;

import java.util.Scanner;

// 댄스 수강 회원에 대한 예외처리
public class A02_Exception {

	@SuppressWarnings("resource")
	public static void main(String[] args) throws DanceException {
		
		Scanner scan = new Scanner(System.in);
		
		int women = 0, men = 0;
		
		System.out.print("댄스학원 여성 회원 수 입력 : ");
		women = scan.nextInt();
		
		System.out.print("댄스학원 남성 회원 수 입력 : ");
		men = scan.nextInt();
		
		if (women == 0)
		{
			throw new DanceException("여성 회원수가 없습니다.");
		}
		else if (men == 0)
		{
			throw new DanceException("남성 회원수가 없습니다.");
		}
		else
			System.out.println("댄스 강의를 시작합니다.");
		
		scan.close();
	}
}
