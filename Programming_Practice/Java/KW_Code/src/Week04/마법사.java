package Week04;

public class ������ {
	int MP, HP, level;
	String charName, hairColor;
	
	public void magicAttack() {
		System.out.println("���׿��� ����Ʈ����.....");
	}
	public void �����������() {
		System.out.println("+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+");
		System.out.println("����\tü��\t����\t����");
		System.out.println(charName + "\t" + HP + "\t" + MP + "\t" + level);		
		System.out.println("+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+");
	}
	public static void main(String[] args) {
		������ mk = new ������();
		
		mk.charName = "ö����";
		mk.HP = 1000;
		mk.MP = 500;
		mk.hairColor = "���";
		mk.level = 1;
		
		mk.�����������();		
		mk.magicAttack();
	}
}













