package �İ�2A;

public class �ǿ��� { // public ���� -> �ٸ� ��ü���� �������� ����(.)�� �� �ִ� Ű����
		public String address;
		private int age;
		protected boolean girl;
		
		public void �����ñ�() {
			System.out.println("ó��ó�� �Ѻ��� �ַ���.");
		}
		
		public int getAge()
		{
			return age;
		}
		
		public void setAge(int age)
		{
			if (age >= 20 && age <= 30)
				this.age = age;
			else
				this.age = 26;
		}
}
