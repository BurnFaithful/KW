package Week12;

import java.io.*;

public class A03_Exception {

	public static void main(String[] args) throws IOException {
		
		FileReader in = null;
		
		in = new FileReader("c:\\windows\\system.ini");
		// File 내부의 문자를 가져올 때는 전부 ASCII 코드 값으로 한 글자씩 가져온다.
		int c;
		while ((c = in.read()) != -1)
		{
			System.out.print((char)c);
		}
		in.close();
		
		/*try {
			in = new FileReader("C:\\windows\\system.ini");
			// File 내부의 문자를 가져올 때는 전부 ASCII 코드 값으로 한 글자씩 가져온다.
			int c;
			while ((c = in.read()) != -1)
			{
				System.out.print((char)c);
			}
			in.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.err.println("경로에 system.ini이 없거나 읽을 수 없습니다.");
		}*/
	}
}
