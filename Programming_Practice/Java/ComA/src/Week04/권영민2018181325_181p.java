package Week04;

class Number
{
	int n; // 인스턴스 변수 n
	
	// 생성자에서 인스턴스 변수 n을 초기화.
	public Number(int n)
	{
		this.n = n;
	}
}

public class 권영민2018181325_181p {
	
	// 매개변수 값에 10을 더하는 메소드
	static void plusTen(Number x)
	{
		x.n += 10;
	}
	
	public static void main(String[] args) {
		Number ob = new Number(5); // Number 객체의 인스턴스 변수 n의 값을 생성자를 통해 초기화.
		plusTen(ob); // 10을 더하는 메소드 호출
		System.out.println(ob.n); // Number 객체 인스턴스 변수 초기값 5에 10을 더해 15를 출력.
	}
}
