package Week04;
class ���̸� {
	String name;  //�ν��Ͻ� ����(instance variable)
	int age;      //�Ӽ�, Ư��
	double height;
	
	public void sleep() {
		System.out.println("����/�̳��� ��ٷ���");
	}
	public void info() {
		System.out.println("�̸�:" + name + ",����:" + age + ",Ű:" + height);
	}
}
public class A01_Objects01 {
	public static void main(String[] args) {
		//��ü������ �ؼ� ���� �������α׷��� �ڵ��ϴ� ����
		���̸� ���뱹 = new ���̸�(); //��ü ���� == object instance
		
		���̸� �� = new ���̸�();
		
		//���뱹�̶�� �ϴ� ������ ���̸���ü�� ������.
		//���뱹 ���� -> Ŭ���� ����, ���۷��� ����, ���� ����

		���뱹.name = "�������";
		���뱹.age = 21;
		���뱹.height = 165;
		
		���뱹.info();
		
	}
}












	