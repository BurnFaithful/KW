package Week11;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

@SuppressWarnings("serial")
public class MyKey extends JFrame {

	JTextField txt;
	JTextArea area;
	
	public MyKey() {
		
		this.setTitle("Key Event");
		this.setSize(640, 480);
		this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		this.setLocationRelativeTo(null);
		this.setLocation(1100, 150);
		this.setLayout(new BorderLayout());
		
		txt = new JTextField(20);
		area = new JTextArea(20, 20);
		area.setEditable(false);
		
		txt.addKeyListener(new KeyListener() {

			@Override
			public void keyPressed(KeyEvent arg0) {}

			@Override
			public void keyReleased(KeyEvent arg0) 
			{
				int key = arg0.getKeyCode();
				
				if (key == KeyEvent.VK_ENTER)
				{
					String str = txt.getText();
					area.setText(area.getText() + str + "\n");
					txt.setText("");
				}
			}

			@Override
			public void keyTyped(KeyEvent arg0) {}
			
		});
		
		
		this.add(txt, BorderLayout.NORTH);
		this.add(area, BorderLayout.CENTER);
		this.setVisible(true);
	}
}
