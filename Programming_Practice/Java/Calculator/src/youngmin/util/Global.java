package youngmin.util;

public class Global {

	private static Global instance;
	
	private Global() {}
	
	public static Global getInstance()
	{
		if (instance == null)
		{
			synchronized (Global.class)
			{
				if (instance == null)
					instance = new Global();
			}
		}
			
		return instance;
	}
	
	public final String strEmpty = " "; // 구분을 위한 공백문자
}
