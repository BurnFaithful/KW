package youngmin.calculator.gui;

import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class SelectFrame extends BaseFrame {
	
	private JButton keyCalcFrameBtn, buttonCalcFrameBtn;
	
	public SelectFrame()
	{
		super.setFrame(320, 240, "Youngmin's Calcultor");
	}
	
	@Override
	public void setComponent() {
		// TODO Auto-generated method stub
		keyCalcFrameBtn = new JButton("키 입력 계산기");
		buttonCalcFrameBtn = new JButton("<html><body>버튼 입력 계산기<br>&nbsp;(일반 계산기)</body></html>");
	}

	@Override
	public void design() {
		// TODO Auto-generated method stub
		keyCalcFrameBtn.setFont(new Font("굴림", Font.BOLD, 15));
		buttonCalcFrameBtn.setFont(new Font("굴림", Font.BOLD, 15));
		
		super.setLayout(new GridLayout());
		super.add("Center", keyCalcFrameBtn);
		super.add(buttonCalcFrameBtn);
	}

	@Override
	public void event() {
		// TODO Auto-generated method stub
		keyCalcFrameBtn.addActionListener(new ButtonClickEvent());
		buttonCalcFrameBtn.addActionListener(new ButtonClickEvent());
	}
	
	class ButtonClickEvent implements ActionListener
	{
		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			if (e.getSource().equals(keyCalcFrameBtn))
			{			
				KeyInputCalcFrame keyInputFrame = new KeyInputCalcFrame();
			}
			else if (e.getSource().equals(buttonCalcFrameBtn))
			{		
				StandardCalcFrame buttonClickFrame = new StandardCalcFrame();
			}
		}	
	}
}
