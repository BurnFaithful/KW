package Week05;
class 정적메소드 {
	public static void display() {
		System.out.println("화질이 좋습니다.!!!");
	}
	public static double circle(int r) {
		return r * r * Math.PI;
	}	
}
public class A02_StaticMethod {
	public static void main(String[] args) {
		정적메소드.display();
		int r = 5;
		System.out.println( 정적메소드.circle(r) );
		System.out.println(Math.PI);
	}
}
