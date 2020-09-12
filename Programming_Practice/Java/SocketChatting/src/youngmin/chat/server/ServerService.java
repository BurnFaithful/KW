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
			System.out.println("===== 채팅 서버 =====");
			System.out.println("클라이언트 접속 대기중 ...");
			
			while (true)
			{
				// 클라이언트 요청 대기
				Socket clSocket = svSocket.accept();
				System.out.println("[ " + clSocket.getInetAddress() + " ] 클라이언트가 접속하였습니다.");
					
				server.addSocket(clSocket);

// region : 서버-클라 1:1 채팅 Console 확인용 → 클라이언트가 보낸 데이터를 서버에 출력
//				String receiveData;
//				
//				BufferedReader tempBuffer = new BufferedReader(new InputStreamReader(clSocket.getInputStream()));
//				while (true)
//				{
//					receiveData = tempBuffer.readLine();
//					if (receiveData == null)
//					{
//						System.out.println("[ " + clSocket.getRemoteSocketAddress() + " ] 클라이언트와의 접속이 끊어졌습니다.");
//						break;
//					}
//					else
//					{
//						System.out.println("클라이언트 : " + receiveData);
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
