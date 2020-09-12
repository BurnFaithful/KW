package Week04;

public class A02_Objects02 {
	public static void main(String[] args) {
		Wizard mk = new Wizard();
		
		mk.name = "Á¸¹ý";
		mk.HP = 500;
		mk.MP = 1000;
		mk.hairColor = "ÇÏ´Ã»ö";
		mk.level = 1;
		
		mk.UnitInfo();
		
		mk.MagicAttack();
	}
}
