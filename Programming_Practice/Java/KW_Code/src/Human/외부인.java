package Human;
import Robot.태권브이;
public class 외부인 {	
	public 외부인() {		
		태권브이 v2 = new 태권브이();
		//v2.girl; 접근불가
		//태권브이에 girl 변수가 protected
		//이기때문에 접근할 수 없음.
		//protected => 같은 패키지안에서만.
	}
}
