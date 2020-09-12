package youngmin.chat.server;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Vector;

public class Server {

	private ArrayList<Socket> socketList;
	
	public Server()
	{
		socketList = new ArrayList<Socket>();
	}
	
	public void addSocket(Socket _socket)
	{
		this.socketList.add(_socket);
		Thread receiverThread = new Thread(new ReceiverThread(_socket));
		receiverThread.start();
	}
	
	class ReceiverThread implements Runnable
	{
		private Socket socket;
		
		public ReceiverThread(Socket _socket)
		{
			socket = _socket;
		}
		
		// �� Ŭ���̾�Ʈ�� ��ε�ĳ��Ʈ�ϴ� ������
		@Override
		public void run() {
			BufferedReader tempBuffer = null;
			String sendMsg;
			
			try
			{
				tempBuffer = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			
				while ((sendMsg = tempBuffer.readLine()) != null)
				{			
					//System.out.println(sendMsg);
					
					Socket tempSocket = null;
					// Ŭ���̾�Ʈ���� �޾ƿ� �����͸� �� Ŭ���̾�Ʈ�� ����(Broadcasting)
					try
					{
						for (int i = 0; i < socketList.size(); i++)
						{
							tempSocket = socketList.get(i);
							
							if (socket.equals(tempSocket)) continue;
							
							BufferedWriter sendWriter = new BufferedWriter(new OutputStreamWriter(tempSocket.getOutputStream()));
							sendWriter.write(sendMsg + "\n");
							sendWriter.flush();
						}
					}
					catch (Exception e)
					{
						System.out.println(" [ " + tempSocket.getInetAddress() +" ] ���� ����.");
						socketList.remove(tempSocket);
						//e.printStackTrace();
					}
				}	
			}
			catch (Exception e)
			{
				e.printStackTrace();
			}
			finally
			{
				try
				{
					System.out.println(" [ " + socket.getInetAddress() + " ] ���� ����.");
					socketList.remove(socket);
					
					System.out.println("������ �� : " + socketList.size());
					
//					if (tempBuffer != null) tempBuffer.close();
//					if (sendWriter != null) sendWriter.close();
					if (socket != null) socket.close();
				}
				catch (Exception e)
				{
					e.printStackTrace();
				}
			}
		}	
	}
	
}
