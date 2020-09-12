package Week10;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

@SuppressWarnings("serial")
public class MYF02 extends JFrame /*implements ActionListener*/ {
	
	private JButton loginBtn, logoutBtn;
	
	public MYF02() 
	{
		this.setTitle("OOP Lecture");
		this.setSize(640, 480);
		
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		
		this.setLayout(new FlowLayout());
		
		loginBtn = new JButton("Login");
		loginBtn.addActionListener(e ->
		{
			JOptionPane.showMessageDialog(null, "�α��� ��ư Ŭ��");
			loginBtn.setText("LOGIN");
		});
		this.add(loginBtn);
		
		logoutBtn = new JButton("Logout");
		logoutBtn.addActionListener(new ActionListener()
		{
			@Override
			public void actionPerformed(ActionEvent e)
			{
				JOptionPane.showMessageDialog(null, "�α׾ƿ� ��ư Ŭ��");
				logoutBtn.setBackground(Color.yellow);
			}
		});
		this.add(logoutBtn);
		
		
		this.setVisible(true);
	}

//	@Override
//	public void actionPerformed(ActionEvent e) {
//		// TODO Auto-generated method stub
//		//JOptionPane.showMessageDialog(null, "��ư Ŭ��");
//		
//		if (e.getSource().equals(loginBtn))
//		{
//			JOptionPane.showMessageDialog(null, "�α��� ��ư Ŭ��");
//		}
//		else if (e.getSource().equals(logoutBtn))
//		{
//			JOptionPane.showMessageDialog(null, "�α׾ƿ� ��ư Ŭ��");
//		}
//	}
}
