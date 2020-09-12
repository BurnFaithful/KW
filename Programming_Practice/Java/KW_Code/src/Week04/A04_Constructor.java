package Week04;

class RedHeadDuck {
	int duckWidth;
	int duckHeight;
	
	public RedHeadDuck() { //생성자 괄호안에 아무것도 없는 경우를 기본 생성자라고 함.
		 duckWidth = 100;
		 duckHeight = 100;
	}
	public RedHeadDuck(int w, int h) {
		duckWidth = w;
		duckHeight = h;
	}
	public void duckInfo() {
		System.out.println("붉은머리 오리의 가로길이는 " + duckWidth);
		System.out.println("붉은머리 오리의 세로길이는 " + duckHeight);
	}	
}
public class A04_Constructor {
	public static void main(String[] args) {
		RedHeadDuck 미친오리 = new RedHeadDuck();
		미친오리.duckInfo();
		
		RedHeadDuck 유저오리 = new RedHeadDuck(300,200);
		유저오리.duckInfo();
	}
}









