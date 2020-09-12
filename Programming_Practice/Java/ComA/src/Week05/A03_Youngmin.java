package Week05;

public class A03_Youngmin {
	public static void main(String[] args) {
		
		System.out.print("아무 숫자나 넣어주세요 >> ");
		
		int number = YScan.scan.nextInt();
		
		System.out.println("입력한 숫자는 " + number + " 입니다.");
		
		System.out.println("x : " + YScan.scan.hashCode());
	}
}
