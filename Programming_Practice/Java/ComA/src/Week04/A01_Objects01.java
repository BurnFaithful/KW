package Week04;

class 아이린 {
	// 인스턴스 변수(instance variable)
	// 속성, 특성
	String name;
	int age;
	double height;
	
	public void Sleep() {
		System.out.println("미인/미남은 잠꾸러기");
	}
	public void info() {
		System.out.println("이름 : " + name);
		System.out.println("나이 : " + age);
		System.out.println("키 : " + height);
	}
}

public class A01_Objects01 {
	// 파일명과 동일한 이름의 클래스는 항상 main 함수를 가지며, 그 이외의 클래스는 public class가 아니게 정의한다.
	public static void main(String[] args) {
		// 객체 생성을 해서 실제 어플리케이션을 코딩하는 영역
		아이린 obj = new 아이린(); // 객체 생성(Object Instance)
		// obj 변수가 아이린 객체를 제어
		// obj 변수 -> 클래스 변수, 참조 변수, 레퍼런스 변수*
		obj.name = "간장게장";
		obj.age = 21;
		obj.height = 165;
		
		obj.info();
		obj.Sleep();
		
		
	}
}
