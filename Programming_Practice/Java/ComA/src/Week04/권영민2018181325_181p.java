package Week04;

class Number
{
	int n; // �ν��Ͻ� ���� n
	
	// �����ڿ��� �ν��Ͻ� ���� n�� �ʱ�ȭ.
	public Number(int n)
	{
		this.n = n;
	}
}

public class �ǿ���2018181325_181p {
	
	// �Ű����� ���� 10�� ���ϴ� �޼ҵ�
	static void plusTen(Number x)
	{
		x.n += 10;
	}
	
	public static void main(String[] args) {
		Number ob = new Number(5); // Number ��ü�� �ν��Ͻ� ���� n�� ���� �����ڸ� ���� �ʱ�ȭ.
		plusTen(ob); // 10�� ���ϴ� �޼ҵ� ȣ��
		System.out.println(ob.n); // Number ��ü �ν��Ͻ� ���� �ʱⰪ 5�� 10�� ���� 15�� ���.
	}
}
