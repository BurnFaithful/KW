package youngmin.chat.server;

import java.net.ServerSocket;
import java.net.Socket;

public class ServerService {
	
	protected final int portNum = 8080;
	
	private Server server;
	
	private ServerSocket svSocket = null;
	
	public ServerService()
	{			
		server = new Server();
		
		try
		{		
			svSocket = new ServerSocket(portNum);
			System.out.println("===== ä�� ���� =====");
			System.out.println("Ŭ���̾�Ʈ ���� ����� ...");
			
			while (true)
			{
				// Ŭ���̾�Ʈ ��û ���
				Socket clSocket = svSocket.accept();
				System.out.println("[ " + clSocket.getInetAddress() + " ] Ŭ���̾�Ʈ�� �����Ͽ����ϴ�.");
					
				server.addSocket(clSocket);

// region : ����-Ŭ�� 1:1 ä�� Console Ȯ�ο� �� Ŭ���̾�Ʈ�� ���� �����͸� ������ ���
//				String receiveData;
//				
//				BufferedReader tempBuffer = new BufferedReader(new InputStreamReader(clSocket.getInputStream()));
//				while (true)
//				{
//					receiveData = tempBuffer.readLine();
//					if (receiveData == null)
//					{
//						System.out.println("[ " + clSocket.getRemoteSocketAddress() + " ] Ŭ���̾�Ʈ���� ������ ���������ϴ�.");
//						break;
//					}
//					else
//					{
//						System.out.println("Ŭ���̾�Ʈ : " + receiveData);
//					}
//				}
// endregion
			}
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {		
		new ServerService();
	}
}
