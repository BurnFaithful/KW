package Week05;

class 컴퓨터 {	
	static 컴퓨터 computer = null;
	
	private 컴퓨터() {
		if (computer == null) {
			computer = new 컴퓨터();
		}
		System.out.println("컴퓨터 객체 생성");
	}
	public void 출력이나해라() {
		System.out.println("유일한 객체이니라~~~~~");
	}
}
public class A04_SingleTon {
	public static void main(String[] args) {
		컴퓨터.computer.출력이나해라();
	}
}




