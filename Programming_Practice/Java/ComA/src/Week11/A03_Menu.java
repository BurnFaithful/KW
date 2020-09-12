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
		
		label = new JLabel("�޴� ���ÿ� ���� �� ������ �ٲ��.");
		menuBar = new JMenuBar();
		JMenu fileMenu = new JMenu("����");
		JMenuItem newItem = new JMenuItem("�� ����");
		JMenuItem openItem = new JMenuItem("����");
		JMenuItem closeItem = new JMenuItem("�ݱ�");
		
		JMenu editMenu = new JMenu("����");
		JMenuItem copyItem = new JMenuItem("�����ϱ�");
		JMenuItem cutItem = new JMenuItem("�߶󳻱�");
		JMenuItem pasteItem = new JMenuItem("�ٿ��ֱ�");
		JMenuItem chatItem = new JMenuItem("ä���ϱ�");
		
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
				label.setText("�� ������ �������ϴ�.");
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
