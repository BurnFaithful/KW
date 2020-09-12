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
				System.out.print("���� �Է�: ");
				int num = scan.nextInt();				
			} catch (Exception e) {
				System.out.println("�߸��Է�!");
				scan.next();
				continue;
			}
			System.out.println("������!");
			break;		
		}
	}	
	
	public static boolean isNumber(String number){		
	    try {
	    	Integer.parseInt(number);  //  "��", "10"	    	
	    	return true;
	    }catch (Exception e) {
	    	
			return false;
		}	    
	}
	
	
	// ���ĺ����� �Ǻ�?
	private static boolean isAlphabet(char ch) {
		// 65~90 , 97,122
		if ((int) ch >= 65 && (int) ch <= 90 || (int) ch >= 97 && (int) ch <= 122) {
			return true;
		} else
			return false;
	}

	// �ΰ��� ���ڸ� �־ ���ڹ����� ������ ���ϴ� �޼ҵ� ����: �տ� ���ڰ� �޿� ���ں��� ������ �ȵ�.
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
