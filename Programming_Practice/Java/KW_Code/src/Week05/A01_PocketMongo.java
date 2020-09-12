package Week05;

import java.util.Scanner;

class 피카츄 {
	public String skinColor;
	public int level;
	
	//생성자 -> 클래스 이름과 동일함,  리턴유형이 아예없음,  매개변수는 0개 이상, 여러개의 생성자 존재함.
	public 피카츄() {		
		this.skinColor = "노란색";
		this.level = 1;		
		System.out.println("피카츄 색깔: " + skinColor);
		System.out.println("피카츄 레벨: " + level);
	}
	public 피카츄(String skinColor, int level) { //생성자 오버로딩(오버로드)
		this.skinColor = skinColor;
		this.level = level;
		System.out.println("피카츄 색깔: " + skinColor);
		System.out.println("피카츄 레벨: " + level);
	}
}
public class A01_PocketMongo {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("======== 포캣몬고 게임 ========");
		System.out.println("1. 기본 피카츄 생성");
		System.out.println("2. 사용자 지정 피카츄 생성");
		System.out.print("선택(종료3번)>> ");
		int cho = scan.nextInt();
		
		switch (cho) {
		case 1: 
			System.out.println("피카츄 포켓몬스터가 기본으로 생성되었음!!!");
			new 피카츄();  
			break;
		case 2:
			System.out.println("사용자가 직접 디자인하는 피카츄 포켓몬스터 생성!!!");
			System.out.print("기본 피부색은? ");
			String skinColor = scan.next();
			System.out.print("포켓몬스터 기본레벨은? ");
			int level = scan.nextInt();					
			new 피카츄(skinColor, level);			
			break;
		default:
			System.out.println("게임 종료!!!");
			System.exit(1); //프로그램 강제 종료.
			break;
		}
		
		scan.close();
	}
}



















