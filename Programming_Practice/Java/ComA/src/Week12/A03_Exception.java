package Week12;

import java.io.*;

public class A03_Exception {

	public static void main(String[] args) throws IOException {
		
		FileReader in = null;
		
		in = new FileReader("c:\\windows\\system.ini");
		// File ������ ���ڸ� ������ ���� ���� ASCII �ڵ� ������ �� ���ھ� �����´�.
		int c;
		while ((c = in.read()) != -1)
		{
			System.out.print((char)c);
		}
		in.close();
		
		/*try {
			in = new FileReader("C:\\windows\\system.ini");
			// File ������ ���ڸ� ������ ���� ���� ASCII �ڵ� ������ �� ���ھ� �����´�.
			int c;
			while ((c = in.read()) != -1)
			{
				System.out.print((char)c);
			}
			in.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.err.println("��ο� system.ini�� ���ų� ���� �� �����ϴ�.");
		}*/
	}
}
