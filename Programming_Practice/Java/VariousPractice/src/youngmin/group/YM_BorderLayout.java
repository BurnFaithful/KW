package youngmin.group;

import java.awt.*;
import javax.swing.*;

class YM_Frame extends JFrame
{
	JButton eBtn, wBtn, nBtn, sBtn, cBtn;
	
	public YM_Frame()
	{
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//this.setLocationRelativeTo(null);
		this.setTitle("BorderLayout ����");
		this.setSize(640, 480);
		this.setLayout(new BorderLayout(50, 50));
	
		eBtn = new JButton("mul");
		wBtn = new JButton("div");
		nBtn = new JButton("add");
		sBtn = new JButton("sub");
		cBtn = new JButton("Calculate");

		this.add(eBtn, BorderLayout.EAST);
		this.add(wBtn, BorderLayout.WEST);
		this.add(nBtn, BorderLayout.NORTH);
		this.add(sBtn, BorderLayout.SOUTH);
		this.add(cBtn, BorderLayout.CENTER);
		
		//this.pack();
		this.setVisible(true);
	}
}

public class YM_BorderLayout {

	public static void main(String[] args) {
		
		new YM_Frame();
	}
}


