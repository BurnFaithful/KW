package �İ�2A;

public class �ǿ��� {  //public ���� -> �ٸ� ��ü���� �������� ����(.)�� �� �ִ� Ű���� 
	String address; //���� ���
	private int age = 26;  //26
	protected boolean girl;  //���� == false
	
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
	
	public void �����ñ�() {
		System.out.println("ó��ó�� �Ѻ��� �ַ���.");
	}	
}
