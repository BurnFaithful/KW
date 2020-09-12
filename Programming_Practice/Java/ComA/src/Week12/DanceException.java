package Week12;

import java.awt.FlowLayout;

import javax.swing.*;

@SuppressWarnings("serial")
class DanceWin extends JFrame
{
	public DanceWin(String msg)
	{
		this.setSize(320, 240);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		this.setLayout(new FlowLayout());
		
		JLabel lbl = new JLabel();
		lbl.setText(msg);
		this.add(lbl);
		
		this.setVisible(true);
	}
}

@SuppressWarnings("serial")
public class DanceException extends Exception {

	public DanceException(String msg) 
	{
		new DanceWin(msg);
	}
}
