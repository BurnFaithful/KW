package Week04;

public class A02_Objects02 {
	public static void main(String[] args) {
		Wizard mk = new Wizard();
		
		mk.name = "����";
		mk.HP = 500;
		mk.MP = 1000;
		mk.hairColor = "�ϴû�";
		mk.level = 1;
		
		mk.UnitInfo();
		
		mk.MagicAttack();
	}
}
