package Week10;

import java.awt.*;

import javax.swing.*;

@SuppressWarnings("serial")
public class MYF03 extends JFrame {
	
	JButton eBtn, wBtn, nBtn, sBtn, cBtn;
	
	public MYF03()
	{
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		this.setTitle("OOP Lecture");
		this.setSize(640, 480);
		this.setLayout(new BorderLayout());
	
		eBtn = new JButton("EAST Button");
		wBtn = new JButton("WEST Button");
		nBtn = new JButton("NORTH Button");
		sBtn = new JButton("SOUTH Button");
		cBtn = new JButton("CENTER Button");

		this.add(eBtn, BorderLayout.EAST);
		this.add(wBtn, BorderLayout.WEST);
		this.add(nBtn, BorderLayout.NORTH);
		this.add(sBtn, BorderLayout.SOUTH);
		this.add(cBtn, BorderLayout.CENTER);
		
		eBtn.addActionListener(e -> 
		{
			eBtn.setBackground(Color.pink);
		});
		
		wBtn.addActionListener(e -> 
		{
			wBtn.setFont(new Font("궁서체", Font.BOLD, 20));
		});
		
		nBtn.addActionListener(e -> 
		{
			nBtn.setText("북쪽 버튼 클릭 완료");
		});
		
		sBtn.addActionListener(e -> 
		{
			JOptionPane.showMessageDialog(null, "남쪽 버튼 클릭 완료");
		});
		
		cBtn.addActionListener(e -> 
		{
			cBtn.setToolTipText("센터입니다~~");
		});
		
		this.setVisible(true);
	}
}
