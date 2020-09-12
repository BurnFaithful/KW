package Week04;

public class A02_Objects02 {
	public static void main(String[] args) {
		마법사 mk = new 마법사();
		
		mk.charName = "철만이";
		mk.HP = 1000;
		mk.MP = 500;
		mk.hairColor = "흰색";
		mk.level = 1;
		
		mk.마법사상세정보();
		
		mk.magicAttack();
	}
}






