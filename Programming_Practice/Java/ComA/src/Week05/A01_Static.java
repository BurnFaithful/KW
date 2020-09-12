package Week05;

class 방송국 {
	public static int KBS1 = 9, KBS2 = 7, SBS = 6, MBC = 11, JTBC = 15, EBS = 13;
}

public class A01_Static {
	public static void main(String[] args) {
		// 메모리는 정적 영역(Static), 동적 영역(Heap), 스택 영역
		// 동적 영역 -> new로 생성된 객체가 적재됨.
		// 정적 영역 -> 컴파일 이후, 프로그램 실행 전에 변수 또는 메소드가 적재되는 곳.
		//			프로그램 종료때까지 메모리에서 유지가 됨.
		//			전체 프로그램에서 딱 한 개만 존재함.
		
		System.out.println("지금부터 방송국 채널을 안내하겠습니다.");
		
		System.out.println("한국방송은 " + 방송국.KBS1 + ", " + 방송국.KBS2 + " 채널!");
		System.out.println("문화방송은 " + 방송국.MBC + " 채널!");
		System.out.println("서울방송은 " + 방송국.SBS + " 채널!");
		System.out.println("교육방송은 " + 방송국.EBS + " 채널!");
		
		System.out.println("수학이 가장 싫어요!!!!");
		System.out.println(Math.abs(-3));
	}
}
