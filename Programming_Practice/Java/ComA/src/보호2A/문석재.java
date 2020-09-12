package 보호2A;

import 컴공2A.권영민;

public class 문석재 {

	public 문석재() {
		// TODO Auto-generated constructor stub
		권영민 ym = new 권영민();
		ym.setAge(27);
//		ym.girl = true;
		
		ym.술마시기();
		System.out.println("나이는 " + ym.getAge());
//		System.out.println("여자친구는 아이린 일까 ? " + ym.girl);
		
		
	}
	
	public static void main(String[] args) {
		new 문석재();	
	}
}
