package Week05;

class Group {
	public Group() {
		Member mem = new Member();
		mem.tel = "01000002222";
		mem.address = "���� ����� ���赿";
		mem.email = "msj8086@nate.com";
		
		mem.setPass("1321321wqwrwerew");
	}
}

public class Member {
	private String id;
	private String pass;
	private String name;
	public String tel;
	public String address;
	public String email;
	
	public String getPass() {
		return pass;
	}
	
	public void setPass(String pass) {
		this.pass = pass;
	}
	
	
}














