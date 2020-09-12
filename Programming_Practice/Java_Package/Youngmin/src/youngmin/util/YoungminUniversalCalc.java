package youngmin.util;

public class YoungminUniversalCalc {
	
	public static void main(String[] args) {
		
		//youngmin.calc.YoungminCalc ymCalc = new youngmin.calc.YoungminCalc();
		PerfectCalc ymPCalc = new PerfectCalc();
		
		int resAdd = ymPCalc.addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
		System.out.println("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = " + resAdd);
		
		int resSub = ymPCalc.subtraction(1, 2, 3);
		System.out.println("1 - 2 - 3 = " + resSub);
		
		int resMul = ymPCalc.multiplication(1, 2, 3, 4, 5);
		System.out.println("1 * 2 * 3 * 4 * 5 = " + resMul);
		
		float resDiv = ymPCalc.Division(5, 0);
		System.out.println("5 / 0 = " + resDiv);
	}
}
