package youngmin.calculator;

import java.util.Stack;
import java.util.StringTokenizer;

import youngmin.util.Global;

enum OperatorType
{
	NONE,
	OPENBRACKET,
	CLOSEBRACKET,
	ARITHMETIC
}

enum PriorityValue
{
	BASE,
	ADD_SUB,
	MUL_DIV
}

public class Convert {

	private Stack<String> operatorStack;
	
	private String oprRegex;
	private String[] oprToken;
	private boolean isOperand;
	
	public Convert()
	{
		operatorStack = new Stack<String>();
		
		oprRegex = "(|+|-|*|/|)";
		oprToken = oprRegex.split("\\|");
		
		isOperand = true;
	}
	
	public boolean getIsOperand()
	{
		return isOperand;
	}
	
	public void setIsOperand(boolean _isOperand)
	{
		isOperand = _isOperand;
	}
	
	public String getOprRegex()
	{
		return oprRegex;
	}
	
	public String[] getOprToken()
	{
		return oprToken;
	}
	
	/*
	 피연산자는 그대로 출력.
	 연산자를 만나면 top의 연산자가 만난 연산자보다 우선순위가 낮으면 push, 그렇지 않으면 pop을 반복.
	 */
	public StringBuilder infix2Postfix(String infixExp)
	{
		StringBuilder postfixExp = new StringBuilder();
		String tempExpToken = null;
		StringTokenizer expToken = new StringTokenizer(infixExp, oprRegex, true/*delimiter도 tokenize*/);
		
		while (expToken.hasMoreTokens())
		{
			tempExpToken = expToken.nextToken();
			isOperand = true;
			
			// operator check
			OperatorType operatorType = checkOperator(tempExpToken, oprToken);
			switch (operatorType)
			{
			case OPENBRACKET:
				pushOperator(tempExpToken);
				break;
			case CLOSEBRACKET:
				closedBracket(postfixExp);
				break;
			case ARITHMETIC:
				arithmeticOperator(postfixExp, tempExpToken);
				break;
			default:
				break;
			}
			
			// operand check
			if (isOperand) postfixExp.append(tempExpToken).append(Global.getInstance().strEmpty);
		}
		while (!operatorStack.isEmpty())
			postfixExp.append(operatorStack.pop()).append(Global.getInstance().strEmpty);
		
		
		return postfixExp;
	}
	
	public OperatorType checkOperator(String _expToken, String[] _oprToken)
	{
		OperatorType operatorType = OperatorType.NONE;
		
		for (int i = 0; i < _oprToken.length; i++)
		{
			if (_expToken.equals(_oprToken[i]))
			{
				switch (_expToken)
				{
				case "(":
					operatorType = OperatorType.OPENBRACKET;
					break;
				case ")":
					operatorType = OperatorType.CLOSEBRACKET;
					break;
				default:
					operatorType = OperatorType.ARITHMETIC;
					break;
				}
				break;
			}
		}
		
		return operatorType;
	}
	
	public void pushOperator(String _expToken)
	{
		operatorStack.push(_expToken);
		isOperand = false;
	}
	
	public void closedBracket(StringBuilder _postfixExp)
	{
		while (!operatorStack.peek().equals("("))
		{
			_postfixExp.append(operatorStack.pop()).append(Global.getInstance().strEmpty);
		}
		operatorStack.pop();
		isOperand = false;
	}
	
	public void arithmeticOperator(StringBuilder _postfixExp, String _expToken)
	{
		if (operatorStack.isEmpty())
		{
			pushOperator(_expToken);
		}
		else
		{
			do
			{
				// 연산자의 우선순위 비교
				if (getOperatorPriority(operatorStack.peek()) >= getOperatorPriority(_expToken))
				{
					_postfixExp.append(operatorStack.pop()).append(Global.getInstance().strEmpty);
					
					if (operatorStack.isEmpty())
					{
						pushOperator(_expToken);
						break;
					}
				}
				else
				{
					pushOperator(_expToken);
					break;
				}
			} while (!operatorStack.isEmpty());
		}
	}
	
	public int getOperatorPriority(String operator)
	{
		int priority = -1;
		
		switch (operator)
		{
		case "+":
		case "-":
			priority = 1;
			break;
		case "*":
		case "/":
			priority = 2;
			break;
		default:
			break;
		}
		
		return priority;
	}
}
