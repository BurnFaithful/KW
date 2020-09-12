package youngmin.calculator.gui;

import javax.swing.JFrame;

@SuppressWarnings("serial")
public abstract class BaseFrame extends JFrame implements IDesign {

	private static final String DEFAULT_FRAME_NAME = "Frame";
	private static final int DEFAULT_FRAME_WIDTH = 640;
	private static final int DEFAULT_FRAME_HEIGHT = 480;
	
	public void setFrame()
	{
		this.setTitle(DEFAULT_FRAME_NAME);
		this.setSize(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setComponent();
		design();
		event();
		
		this.setVisible(true);
	}
	
	public void setFrame(int w, int h)
	{
		this.setTitle(DEFAULT_FRAME_NAME);
		this.setSize(w, h);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setComponent();
		design();
		event();
		
		this.setVisible(true);
	}
	
	public void setFrame(int w, int h, String name)
	{
		this.setTitle(name);
		this.setSize(w, h);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setComponent();
		design();
		event();
		
		this.setVisible(true);
	}
	
	public void setFrame(int w, int h, String name, int closeOperation)
	{
		this.setTitle(name);
		this.setSize(w, h);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(closeOperation);
		
		setComponent();
		design();
		event();
		
		this.setVisible(true);
	}
}
