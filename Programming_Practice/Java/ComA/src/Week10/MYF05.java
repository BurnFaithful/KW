package Week10;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

@SuppressWarnings("serial")
public class MYF05 extends JFrame {

	private JTextField preOperandField, postOperandField;
	private JTextArea resultTxt;
	private JButton plusBtn;
	
	public MYF05()
	{
		this.setTitle("OOP Lecture : Simple Opeartion");
		this.setSize(640, 480);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		
		this.setLayout(new FlowLayout());
		
		preOperandField = new JTextField(5);
		preOperandField.addFocusListener(new FocusListener()
		{
			@Override
			public void focusGained(FocusEvent arg0) {
				preOperandField.setText("");
			}

			@Override
			public void focusLost(FocusEvent arg0) {
				// TODO Auto-generated method stub
				preOperandField.setText("값 입력");
			}
		});
		
		postOperandField = new JTextField(5);
		postOperandField.addFocusListener(new FocusListener()
		{
			@Override
			public void focusGained(FocusEvent arg0) {
				postOperandField.setText("");
			}

			@Override
			public void focusLost(FocusEvent arg0) {
				// TODO Auto-generated method stub
				postOperandField.setText("값 입력");
			}
		});
		
		resultTxt = new JTextArea(1, 6);
		resultTxt.setEditable(false);
		
		plusBtn = new JButton("+");
		plusBtn.addActionListener(e -> 
		{
			if (preOperandField.getText().equals("") ||
					postOperandField.getText().equals(""))
			{
				JOptionPane.showMessageDialog(null, "값을 입력해주세요.");
			}
			
			int preOperand = Integer.parseInt(preOperandField.getText());
			int postOperand = Integer.parseInt(postOperandField.getText());
			int result = preOperand + postOperand;
			resultTxt.setText(Integer.toString(result));
		});

		this.add(preOperandField);
		this.add(postOperandField);
		this.add(plusBtn);
		this.add(resultTxt);
		
		this.pack(); // 구성요소가 배치된 형태로 전체 윈도우창 크기가 결정됨.
		this.setVisible(true);
	}
}
