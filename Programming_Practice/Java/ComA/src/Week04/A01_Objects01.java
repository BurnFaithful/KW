package Week04;

class ���̸� {
	// �ν��Ͻ� ����(instance variable)
	// �Ӽ�, Ư��
	String name;
	int age;
	double height;
	
	public void Sleep() {
		System.out.println("����/�̳��� ��ٷ���");
	}
	public void info() {
		System.out.println("�̸� : " + name);
		System.out.println("���� : " + age);
		System.out.println("Ű : " + height);
	}
}

public class A01_Objects01 {
	// ���ϸ�� ������ �̸��� Ŭ������ �׻� main �Լ��� ������, �� �̿��� Ŭ������ public class�� �ƴϰ� �����Ѵ�.
	public static void main(String[] args) {
		// ��ü ������ �ؼ� ���� ���ø����̼��� �ڵ��ϴ� ����
		���̸� obj = new ���̸�(); // ��ü ����(Object Instance)
		// obj ������ ���̸� ��ü�� ����
		// obj ���� -> Ŭ���� ����, ���� ����, ���۷��� ����*
		obj.name = "�������";
		obj.age = 21;
		obj.height = 165;
		
		obj.info();
		obj.Sleep();
		
		
	}
}
