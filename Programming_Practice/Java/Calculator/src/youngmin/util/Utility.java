package youngmin.util;

import java.util.regex.Pattern;

public class Utility 
{
	public static boolean isNumeric(String str)
	{
		try
		{
			Double.parseDouble(str);
			return true;	
		}
		catch (NumberFormatException ec)
		{
			//ec.printStackTrace();
			return false;
		}
	}
	
	public static boolean isOperator(String str)
	{
		if (Pattern.matches("(^[0-9]*$)|\\+|-|¡¿|¡À", str))
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}
