package Week05;

class Car {
	private int speed; //ĸ��ȭ �Ǿ� �ִ�. ���� ���� �Ұ�..(�ٸ� ��ü����)

	public void setSpeed(int speed) {  //���͸޼ҵ�(setter)�� �̿��ؼ� speed������ �����ϰ� ��.
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
	public int getSpeed() { //���͸޼ҵ�(getter)�� �̿��ؼ� speed������ ���� ���´�.
		return this.speed;
	}
}
public class A02_CarApple {
	public static void main(String[] args) {
		Car c1 = new Car();	//Car ��ü�� �����ϰ�	
		c1.setSpeed(200);  //c1������ �̿��ؼ� ���͸޼ҵ带 ���� speed���� ����(����)
		System.out.println(c1.getSpeed()); //c1������ �̿��ؼ� speed���� �޾ƿ�(����)
				
		c1.setSpeed(-50);
		System.out.println(c1.getSpeed());
	}
}












