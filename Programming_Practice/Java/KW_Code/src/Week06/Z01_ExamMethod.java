package Week06;

import java.io.IOException;
import java.util.Scanner;

public class Z01_ExamMethod {
	static Scanner scan = new Scanner(System.in);
	
	public static void main(String[] args) {		
		
		isNumber2(); 
	}		
	public static void isNumber2() {
		while(true) {			
			try {
				System.out.print("숫자 입력: ");
				int num = scan.nextInt();				
			} catch (Exception e) {
				System.out.println("잘못입력!");
				scan.next();
				continue;
			}
			System.out.println("숫자임!");
			break;		
		}
	}	
	
	public static boolean isNumber(String number){		
	    try {
	    	Integer.parseInt(number);  //  "ㅁ", "10"	    	
	    	return true;
	    }catch (Exception e) {
	    	
			return false;
		}	    
	}
	
	
	// 알파벳인지 판별?
	private static boolean isAlphabet(char ch) {
		// 65~90 , 97,122
		if ((int) ch >= 65 && (int) ch <= 90 || (int) ch >= 97 && (int) ch <= 122) {
			return true;
		} else
			return false;
	}

	// 두개의 숫자를 넣어서 숫자범위의 총합을 구하는 메소드 조건: 앞에 숫자가 뒷에 숫자보다 작은면 안됨.
	private static int numTotal(int v1, int v2) {
		int total = 0;
		if (v1 >= v2) {
			for (int i = v2; i <= v1; i++) // for(int i = v1; i >= v2; i--)
				total = total + i; // total += i;
		} else if (v1 < v2) {
			for (int i = v1; i <= v2; i++)
				total = total + i; // total += i;
		}
		return total;
	}

	private static boolean isZeroBig(int value) {
		boolean result = false;
		result = (value > 0) ? true : false;
		return result;
	}

	private static boolean flgMax(int n1, int n2) {
		boolean result = false;
		result = (n1 > n2) ? true : false;
		return result;
	}

	private static int moonMax1(int n1, int n2) {
		int result = 0;
		result = (n1 > n2) ? n1 : n2;
		return result;
	}

	private static int moonMax(int n1, int n2) {
		if (n1 > n2)
			return n1;
		else if (n1 < n2)
			return n2;
		else if (n1 == n2)
			return n1;
		else
			return 0;
	}
}
