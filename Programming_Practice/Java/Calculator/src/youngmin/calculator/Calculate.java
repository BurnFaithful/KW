package youngmin.calculator;

import java.util.Stack;
import java.util.StringTokenizer;

import youngmin.util.Global;

public class Calculate {

	private Convert postfixConverter;
	
	private Stack<Integer> operandStack;
	
	public Calculate()
	{
		postfixConverter = new Convert();
		
		operandStack = new Stack<Integer>();
	}
	
	public String getPostfixExpression(String expression)
	{
		String result = postfixConverter.infix2Postfix(expression).toString();
		
		return result;
	}
	
	public int computeOperator(int operand_left, int operand_right, String operator)
	{
		int tempResult = 0;
		
		switch (operator)
		{
		case "+":
			tempResult = operand_left + operand_right;
			break;
		case "-":
			tempResult = operand_left - operand_right;
			break;
		case "*":
			tempResult = operand_left * operand_right;
			break;
		case "/":
			tempResult = operand_left / operand_right;
			break;
		}
		
		return tempResult;
	}
	
	public int calculateInt(String postfixExp)
	{
		StringTokenizer expToken = new StringTokenizer(postfixExp, Global.getInstance().strEmpty);
		String tempExpToken = null;
		
		while (expToken.hasMoreTokens())
		{
			tempExpToken = expToken.nextToken();
			postfixConverter.setIsOperand(true);
			
			for (int i = 0; i < postfixConverter.getOprToken().length; i++)
			{
				if (tempExpToken.equals(postfixConverter.getOprToken()[i]))
				{
					postfixConverter.setIsOperand(false);
					
					// 연산자를 만나면 operandStack에서 피연산자(operand) 2개를 pop하여 계산한 후 push
					if (operandStack.size() >= 2)
					{
						int right = operandStack.pop();
						int left = operandStack.pop();
						
						operandStack.push(computeOperator(left, right, tempExpToken));
						break;
					}
				}
			}
			
			// 피연사자를 만나면 operandStack에 push
			if (postfixConverter.getIsOperand()) operandStack.push(Integer.parseInt(tempExpToken));
		}
		
		return operandStack.pop(); // operandStack에 남은 마지막 element가 계산결과
	}
	
	public float calculateFloat(String postfixExp)
	{	
		return 0.1f;
	}
}
