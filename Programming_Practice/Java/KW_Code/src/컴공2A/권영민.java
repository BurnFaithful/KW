package 컴공2A;

public class 권영민 {  //public 공용 -> 다른 객체에서 언제든지 접근(.)할 수 있는 키워드 
	String address; //서울 사람
	private int age = 26;  //26
	protected boolean girl;  //없으 == false
	
	public int getAge() {
		return this.age;
	}
	
	public void setAge(int age) {
		if ( age >= 20 && age <= 30) {
			this.age = age;
		}
		else {
			this.age = 26;
		}
	}
	
	public void 술마시기() {
		System.out.println("처음처럼 한병이 주량임.");
	}	
}
