package youngmin.chat.gui;

import javax.swing.JFrame;

@SuppressWarnings("serial")
public abstract class BaseFrame extends JFrame implements IAppDesign {
	
	private static final int DEFAULT_FRAME_WIDTH = 640;
	private static final int DEFAULT_FRAME_HEIGHT = 480;
	
	public BaseFrame()
	{
		setTitle("Default Title");
		setSize(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT);

		setFrame();
		designFrame();
		
		setVisible(true);
	}
	
	public BaseFrame(String title)
	{
		setTitle(title);
		setSize(DEFAULT_FRAME_WIDTH, DEFAULT_FRAME_HEIGHT);

		setFrame();
		designFrame();
		
		setVisible(true);
	}
	
	public BaseFrame(String title, int width, int height)
	{
		setTitle(title);
		setSize(width, height);

		setFrame();
		designFrame();
		
		setVisible(true);
	}

	@Override
	public void setFrame() {
		// TODO Auto-generated method stub
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setResizable(false);
	}
	
	public void setFrame(boolean isResize) {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setLocationRelativeTo(null);
		setResizable(isResize);
	}
	
	public void designFrame()
	{
		allocPanel();
		designPanel();
		adaptPanel();
		addEventListener();
	}
}
