package youngmin.group;
import java.util.Scanner;

public class LogicalOperator {
	public static void main(String[] args) {
		// true AND false, true OR true ���� �Է��ϸ� ��� ����ϱ�.
		
		Scanner scan = new Scanner(System.in);
		
		String left, operator, right;
		
		while (true)
		{
			System.out.print("�Է� > ");
			left = scan.next();
			operator = scan.next();
			right = scan.next();
			
			boolean lOperand, rOperand;
			lOperand = Boolean.parseBoolean(left);
			rOperand = Boolean.parseBoolean(right);
			
			switch (operator)
			{
			case "AND":
				System.out.println("����� " + (lOperand && rOperand) + "�Դϴ�.");
				break;
			case "OR":
				System.out.println("����� " + (lOperand || rOperand) + "�Դϴ�.");
				break;
			}
		}
	}
}
