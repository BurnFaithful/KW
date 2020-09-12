package Week05;

import java.util.Scanner;
public class YScan {
	static Scanner scan = new Scanner(System.in);	
	
	public YScan() {
		System.out.println("y: " + scan.hashCode());
	}
	public static void main(String[] args) {
		new YScan();
	}
}
