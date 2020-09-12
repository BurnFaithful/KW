package Robot;

public class 태권브이 {
	public String skill; 
	public String manName;
	//private String girl;
	protected String girl;
	
	public 태권브이() {
		this.skill = "태권도";
		this.manName = "김훈";
		this.girl = "윤영희";
	}
	public void 태권브이정보() {
		System.out.println("태권브이 주기술은 " + this.skill + "임!!");
		System.out.println("태권브이 탑승자는 " + this.manName);		
	}
	
}




