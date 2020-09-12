package Week03;

class 로보트 {
	public void 공격() {
		System.out.println("발로 찬다.");
	}
	public void 비행() {
		System.out.println("추진기로 난다.");
	}
}
class 다간 extends 로보트 {
	
}
class 가오가이거 extends 로보트 {
	@Override
	public void 공격() {
		System.out.println("골디안 해머");
	}
}

public class A07_Class {
	public static void main(String[] args) {
		다간 dg = new 다간();
		dg.공격();
		dg.비행();
		
		가오가이거 g = new 가오가이거();
		g.공격();
		g.비행();
	}
}
