package 컴공2A;

public class 권영민 { // public 공용 -> 다른 객체에서 언제든지 접근(.)할 수 있는 키워드
		public String address;
		private int age;
		protected boolean girl;
		
		public void 술마시기() {
			System.out.println("처음처럼 한병이 주량임.");
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
