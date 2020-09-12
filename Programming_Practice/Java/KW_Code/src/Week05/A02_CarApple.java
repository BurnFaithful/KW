package Week05;

class Car {
	private int speed; //캡슐화 되어 있다. 직접 접근 불가..(다른 객체에서)

	public void setSpeed(int speed) {  //세터메소드(setter)를 이용해서 speed변수를 접근하게 함.
		if (speed > 180) {
			this.speed = 180;
		}
		else if (speed <= 0) {
			this.speed = 0;
		}
		else {
			this.speed = speed; 
		}		
	}
	public int getSpeed() { //게터메소드(getter)를 이용해서 speed변수에 값을 얻어온다.
		return this.speed;
	}
}
public class A02_CarApple {
	public static void main(String[] args) {
		Car c1 = new Car();	//Car 객체를 생성하고	
		c1.setSpeed(200);  //c1변수를 이용해서 세터메소드를 통해 speed값을 설정(저장)
		System.out.println(c1.getSpeed()); //c1변수를 이용해서 speed값을 받아옴(리턴)
				
		c1.setSpeed(-50);
		System.out.println(c1.getSpeed());
	}
}












