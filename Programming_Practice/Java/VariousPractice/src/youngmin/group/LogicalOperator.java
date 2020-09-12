package youngmin.group;
import java.util.Scanner;

public class LogicalOperator {
	public static void main(String[] args) {
		// true AND false, true OR true 등을 입력하면 결과 출력하기.
		
		Scanner scan = new Scanner(System.in);
		
		String left, operator, right;
		
		while (true)
		{
			System.out.print("입력 > ");
			left = scan.next();
			operator = scan.next();
			right = scan.next();
			
			boolean lOperand, rOperand;
			lOperand = Boolean.parseBoolean(left);
			rOperand = Boolean.parseBoolean(right);
			
			switch (operator)
			{
			case "AND":
				System.out.println("결과는 " + (lOperand && rOperand) + "입니다.");
				break;
			case "OR":
				System.out.println("결과는 " + (lOperand || rOperand) + "입니다.");
				break;
			}
		}
	}
}
