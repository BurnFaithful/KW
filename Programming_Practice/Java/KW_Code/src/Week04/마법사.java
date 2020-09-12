package Week04;

public class 마법사 {
	int MP, HP, level;
	String charName, hairColor;
	
	public void magicAttack() {
		System.out.println("메테오를 떨어트린다.....");
	}
	public void 마법사상세정보() {
		System.out.println("+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+");
		System.out.println("존명\t체력\t마력\t레벨");
		System.out.println(charName + "\t" + HP + "\t" + MP + "\t" + level);		
		System.out.println("+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+");
	}
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













