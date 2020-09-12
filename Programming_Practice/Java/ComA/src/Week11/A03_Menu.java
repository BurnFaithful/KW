package Week11;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class A03_Menu {
	public static void main(String[] args) {
		new MyMenu();
	}
}

@SuppressWarnings("serial")
class MyMenu extends JFrame
{
	JLabel label;
	JMenuBar menuBar;
	
	public MyMenu()
	{
		this.setTitle("Menu");
		this.setSize(1024, 768);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(new BorderLayout());
		
		label = new JLabel("메뉴 선택에 따라 이 문장이 바뀐다.");
		menuBar = new JMenuBar();
		JMenu fileMenu = new JMenu("파일");
		JMenuItem newItem = new JMenuItem("새 문서");
		JMenuItem openItem = new JMenuItem("열기");
		JMenuItem closeItem = new JMenuItem("닫기");
		
		JMenu editMenu = new JMenu("편집");
		JMenuItem copyItem = new JMenuItem("복사하기");
		JMenuItem cutItem = new JMenuItem("잘라내기");
		JMenuItem pasteItem = new JMenuItem("붙여넣기");
		JMenuItem chatItem = new JMenuItem("채팅하기");
		
		menuBar.add(fileMenu);
		fileMenu.add(newItem);
		fileMenu.add(openItem);
		fileMenu.addSeparator();
		fileMenu.add(closeItem);
		
		menuBar.add(editMenu);
		editMenu.add(copyItem);
		editMenu.add(cutItem);
		editMenu.add(pasteItem);
		editMenu.add(chatItem);
		
		newItem.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				label.setText("새 문서를 열었습니다.");
			}
			
		});
		
		chatItem.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				MyKey chatFrame = new MyKey();
			}
			
		});
		
		this.add(label, BorderLayout.NORTH);
		this.setJMenuBar(menuBar);
		this.setVisible(true);
	}
}
