package youngmin.generator;


import youngmin.calculator.gui.*;

public class Main {
	
	private SelectFrame selectFrame;
	
	public Main()
	{	
		selectFrame = new SelectFrame();

// Console
//		System.out.print("����� ���� �Է����ּ���(infix) >> ");
//		String expression = KeyScanner.getInstance().nextLine();
//		
//		String result = calculator.getPostfixExpression(expression);
//		System.out.println("postfix �� " + result);
//		System.out.println("����� : " + calculator.calculateInt(result));
	}
	
	public static void main(String[] args) {
		
		new Main();
	}
}
