package Week05;
class �����޼ҵ� {
	public static void display() {
		System.out.println("ȭ���� �����ϴ�.!!!");
	}
	public static double circle(int r) {
		return r * r * Math.PI;
	}	
}
public class A02_StaticMethod {
	public static void main(String[] args) {
		�����޼ҵ�.display();
		int r = 5;
		System.out.println( �����޼ҵ�.circle(r) );
		System.out.println(Math.PI);
	}
}
