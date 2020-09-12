package youngmin.chat.client;

import java.awt.BorderLayout;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

import javax.swing.*;

import youngmin.chat.gui.BaseFrame;

@SuppressWarnings("serial")
public class Client extends BaseFrame {
	
	public static final String WINDOW_TITLE_NAME = "Chatting Program"; 
	public static final int WINDOW_SIZE_WIDTH = 640;
	public static final int WINDOW_SIZE_HEIGHT = 480;
	
	private JPanel txtAreaPanel, uiPanel;
	
	private JScrollPane scrollPane;
	private JTextArea printArea;
	private JTextField inputArea;
	private JButton unconnectBtn;
	
	private Socket clSocket = null;
	
	private BufferedWriter sendWriter = null;
	
	public Client()
	{		
		super(WINDOW_TITLE_NAME, WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT);
		
		try
		{
			clSocket = new Socket("127.0.0.1", 8080);
			
			setBufferedWriter(clSocket);
			
			Thread clientThread = new Thread(new ClientReceiverThread(clSocket));
			clientThread.start();
		}
		catch (Exception e)
		{
			e.printStackTrace();
			printArea.append("[ " + clSocket.getInetAddress() + " ] 클라이언트의 연결이 종료되었습니다.");
		}
	}
	
	public void setClSocket(Socket _socket) { clSocket = _socket; }
	
	public void setBufferedWriter(Socket _socket)
	{
		try
		{
			sendWriter = new BufferedWriter(new OutputStreamWriter(_socket.getOutputStream()));
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
	
	@Override
	public void allocPanel() 
	{
		printArea = new JTextArea("=====GUI 채팅방=====\n", 30, 30);
		inputArea = new JTextField(10);
		unconnectBtn = new JButton("연결 해제");
		scrollPane = new JScrollPane(printArea);
	}

	@Override
	public void designPanel() 
	{
		printArea.setEditable(false);
		
		inputArea.setText("여기에 입력하세요.");
		
		scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
		scrollPane.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
	}

	@Override
	public void adaptPanel() 
	{
		this.add(scrollPane, BorderLayout.CENTER);
		this.add(inputArea, BorderLayout.SOUTH);
		//this.add(unconnectBtn, BorderLayout.EAST);
	}

	@Override
	public void addEventListener() 
	{
		inputArea.addKeyListener(new ClientEvent());
		inputArea.addFocusListener(new ClientEvent());
		
		//unconnectBtn.addActionListener(new ClientEvent());
	}
	
	class ClientEvent implements KeyListener, FocusListener
	{
		@Override
		public void focusGained(FocusEvent e) 
		{
			inputArea.setText("");
		}

		@Override
		public void focusLost(FocusEvent e) 
		{
			inputArea.setText("여기에 입력하세요");
		}

		@Override
		public void keyPressed(KeyEvent arg0) {}

		@Override
		public void keyReleased(KeyEvent arg0) 
		{
			String clientMsg = null;
			
			if (arg0.getKeyCode() == KeyEvent.VK_ENTER)
			{
				clientMsg = inputArea.getText();
				printArea.append(clSocket.getInetAddress() + " : " + clientMsg + "\n");
				inputArea.setText("");
			
				try
				{
					sendWriter.write(clientMsg + "\n");
					sendWriter.flush();
				}
				catch (Exception e)
				{
					e.printStackTrace();
				}
			}
		}

		@Override
		public void keyTyped(KeyEvent arg0) {}	
	}
	
	class ClientReceiverThread implements Runnable
	{
		private Socket socket;
		
		public ClientReceiverThread(Socket _socket)
		{
			socket = _socket;
		}
		
		@Override
		public void run() {
			BufferedReader tempBuffer = null;
			String receiveMsg = null;
			
			try
			{
				tempBuffer = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			
				while (true)
				{
					receiveMsg = tempBuffer.readLine();
					printArea.append("상대 : " + receiveMsg + "\n");
				}
			}
			catch (Exception e)
			{
				e.printStackTrace();
				printArea.append("연결이 끊겼습니다.");
			}
			finally
			{
				try
				{
					if (clSocket != null && !clSocket.isClosed()) clSocket.close();
				}
				catch (Exception e)
				{
					e.printStackTrace();
				}
			}
		}
	}
	
	public static void main(String[] args) {		
		new Client();		
	}
}
