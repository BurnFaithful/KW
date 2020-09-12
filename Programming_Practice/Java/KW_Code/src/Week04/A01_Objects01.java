package Week04;
class 아이린 {
	String name;  //인스턴스 변수(instance variable)
	int age;      //속성, 특성
	double height;
	
	public void sleep() {
		System.out.println("미인/미남은 잠꾸러기");
	}
	public void info() {
		System.out.println("이름:" + name + ",나이:" + age + ",키:" + height);
	}
}
public class A01_Objects01 {
	public static void main(String[] args) {
		//객체생성을 해서 실제 어플프로그램을 코딩하는 영역
		아이린 순대국 = new 아이린(); //객체 생성 == object instance
		
		아이린 폰 = new 아이린();
		
		//순대국이라고 하는 변수가 아이린객체를 제어함.
		//순대국 변수 -> 클래스 변수, 레퍼런스 변수, 참조 변수

		순대국.name = "간장게장";
		순대국.age = 21;
		순대국.height = 165;
		
		순대국.info();
		
	}
}












	