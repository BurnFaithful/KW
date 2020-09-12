package Week11;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

@SuppressWarnings("serial")
public class MyMouse extends JFrame {

	JTextField txtX, txtY, txtState;
	
	public MyMouse() {
		this.setTitle("Mouse Event");
		this.setSize(640, 480);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocation(1100, 150);
		this.setLayout(new FlowLayout());
		
		txtX = new JTextField(10);
		txtY = new JTextField(10);
		txtState = new JTextField(20);
	
	this.addMouseListener(new MouseListener() {
		@Override
		public void mouseClicked(MouseEvent arg0) 
		{
			txtX.setText(Integer.toString(arg0.getX()));
			txtY.setText(Integer.toString(arg0.getY()));
		}

		@Override
		public void mouseEntered(MouseEvent arg0) 
		{
			txtState.setText("Mouse Enter");
		}

		@Override
		public void mouseExited(MouseEvent arg0) 
		{
			txtState.setText("Mouse Exit");
		}

		@Override
		public void mousePressed(MouseEvent arg0) {}

		@Override
		public void mouseReleased(MouseEvent arg0) {}
			
		});
	
	this.add(txtX);
	this.add(txtY);
	this.add(txtState);
	this.setVisible(true);
	}
}
