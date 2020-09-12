package Week06;

import Test.sample;

class AAA {
	public AAA() {
		System.out.println("AAA");
	}
	public AAA(String n) {
		System.out.println("AAA " + n);
	}
}
class BBB extends AAA {
	public BBB() {
		// TODO Auto-generated constructor stub
	}
	public BBB(String n) {
		super(n);
		System.out.println("BBB 두번째 생성자");
	}
}

public class A03_TTT {
	public static void main(String[] args) {
		sample ts = new sample();	
		
		BBB b = new BBB();
		BBB b1 = new BBB("영민");
		
	}
}
