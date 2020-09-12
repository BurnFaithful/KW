package Week04;

import java.util.Scanner;

class 서머너 {
	String name;
	String hairColor = "하얀색";
	String skinColor = "하얀색";
	int level = 1;
	
	public void 서머너상세정보 () {
		System.out.println("생성된 서머너 캐릭이름: " + name);
		System.out.println("헤어칼라:" + hairColor + ",피부색:" + skinColor + ",현재레벨:" + level);
	}
}
public class A04_LostArc {
	public static void main(String[] args) { //클래스들을 이용해서 실제 실행 프로그램 로직코딩하는곳
		Scanner scan = new Scanner(System.in);
		
		서머너 s1 = null;
		boolean  flag = true;
		while(flag) {		
			System.out.println("1. 서머너 초기생성");
			System.out.println("2. 서머너 상세생성");
			System.out.println("3. 캐릭터 생성후 게임시작");
			System.out.print(">> ");
			int menu = scan.nextInt();
			scan.nextLine();
			
			switch (menu) {
			case 1:
				if ( s1 == null ) {
					s1 = new 서머너();
					System.out.print("생성할 이름을 입력하세요>> ");
					s1.name = scan.nextLine();
					System.out.println("초기 " + s1.name + " 서머너 생성됨!!");
				}else {
					System.out.println("이미 서머너 객체가 생성되었음. 상세정보입력");
				}
				break;
			case 2:
				if ( s1 != null) {
					System.out.print("서머너의 머리 색깔 입력하시오>> ");				
					s1.hairColor = scan.nextLine();
					System.out.print("서머너의 피부 색깔 입력하시오>> ");
					s1.skinColor = scan.nextLine();
					s1.level = 10;
					s1.서머너상세정보();
				}else {
					System.out.println("서머너 초기 생성부터 하세요");
				}
				break;
			case 3:	
				if ( s1 == null ) {
					System.out.println("캐릭터 부터 생성하세여~");
				}else {
					flag = false;					
				}
				break;
			}
		}
		System.out.println("이제 서머너로 게임을 시작합니다.");
		
		scan.close();
	}
}






















