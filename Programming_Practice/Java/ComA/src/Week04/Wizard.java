package Week04;

public class Wizard {
	int MP;
	int HP;
	int level;
	String name;
	String hairColor;
	
	public void MagicAttack() {
		System.out.println("���׿��� ����Ʈ���� !!!!");
	}
	
	public void UnitInfo() {
		System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-");
		System.out.println("����\t����\tü��\t����");
		System.out.println(name + "\t" + level + "\t" + HP + "\t" + MP);
		System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-");
	}
}
