package Week03;

public class A05_StringIF {
	public static void main(String[] args) {
		String oldName = "Kwon";
		String newName = "Kwon";
		
		if (oldName.equals(newName)) 
		{
			System.out.println("same");
		}
		else
		{
			System.out.println("other");
		}
		
		if (oldName == newName) 
		{
			System.out.println("�̸��� ����");
		}
		else
		{
			System.out.println("�ٸ� �̸�");
		}
	}
}
