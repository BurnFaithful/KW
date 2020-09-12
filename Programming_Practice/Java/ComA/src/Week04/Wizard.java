package Week04;

public class Wizard {
	int MP;
	int HP;
	int level;
	String name;
	String hairColor;
	
	public void MagicAttack() {
		System.out.println("메테오를 떨어트린다 !!!!");
	}
	
	public void UnitInfo() {
		System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-");
		System.out.println("존명\t레벨\t체력\t마력");
		System.out.println(name + "\t" + level + "\t" + HP + "\t" + MP);
		System.out.println("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-");
	}
}
