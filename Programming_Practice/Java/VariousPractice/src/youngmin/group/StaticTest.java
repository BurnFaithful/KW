package youngmin.group;

class StaticSample
{
	int n;
	static int m;
	
	void g() {}
	static void t() {}
}

public class StaticTest {
	public static void main(String[] args) {
		StaticSample.m = 10;
		System.out.println(StaticSample.m);
		
		StaticSample s1 = new StaticSample();
		StaticSample s2 = new StaticSample();
		
		s1.m++;
		
		System.out.println(s2.m);
	}
}
