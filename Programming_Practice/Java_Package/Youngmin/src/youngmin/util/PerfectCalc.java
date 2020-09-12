package youngmin.util;

import youngmin.calc.YoungminCalc;

public class PerfectCalc extends YoungminCalc {
	
	@Override
	public int addition(int... x)
	{
		int result = super.addition(x);	
		System.out.println("���� ��� : " + result);
		
		return result;
	}
	
	public int multiplication(int x, int y)
	{
		return x * y;
	}
	
	public float Division(int x, int y)
	{
		float result = 0.f;
		
		try
		{
			result = x / y;
		}
		catch (ArithmeticException e)
		{
			System.out.println("0���δ� ���� �� ����.");
			result = 1.f;
		}
		
		return result;
	}
}