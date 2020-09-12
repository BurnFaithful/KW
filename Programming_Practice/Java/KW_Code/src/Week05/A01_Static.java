package Week05;

class 방송국 {
	public static int KBS1 = 9, KBS2 = 7, SBS = 6, MBC = 11, JTBC = 15, EBS = 13;
}

public class A01_Static {
	public static void main(String[] args) {
		System.out.println("지금부터 방송국 채널을 안내하겠습니다.");		
		System.out.println("한국방송은 " + 방송국.KBS1 + ", " + 방송국.KBS2 + "채널!");
		System.out.println("문화방송은 " + 방송국.MBC + "채널!");
		System.out.println("서울방송은 " + 방송국.SBS + "채널!");
		System.out.println("교육방송은 " + 방송국.EBS + "채널!");
		
		System.out.println("수학이 가장 싫어요!!!!");
		System.out.println(Math.abs(-3));
	}
}























