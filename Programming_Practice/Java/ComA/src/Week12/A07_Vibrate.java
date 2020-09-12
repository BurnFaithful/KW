package Week12;

import java.awt.event.*;
import java.util.Random;

import javax.swing.*;

@SuppressWarnings("serial")
class Vibrate extends JFrame implements Runnable
{
	private Thread runThread;
	private int vibrateStrength;
	
	public Vibrate()
	{
		this.setTitle("Vibrating Frame");
		this.setSize(320, 240);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocation(200, 400);
		//this.setLocationRelativeTo(null);
		
		this.setVisible(true);
		
		this.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e)
			{
				if (!runThread.isAlive())
					return;
				
				runThread.interrupt();
			}
		});
		
		vibrateStrength = 5;
		runThread = new Thread(this);
		runThread.start();
	}
	
	public int getVibrateStrength() { return vibrateStrength; }
	public void setVibrateStrength(int strength) { vibrateStrength = strength; }
	
	@Override
	public void run() {
		// TODO Auto-generated method stub
		while (true)
		{
			try
			{
				Thread.sleep(20);
			}
			catch (Exception e)
			{
				return;
			}
			
			Random random = new Random();
			
			int posX = this.getX() + random.nextInt() % vibrateStrength;
			int posY = this.getY() + random.nextInt() % vibrateStrength;
			this.setLocation(posX, posY);
		}
	}
}

public class A07_Vibrate {

	public static void main(String[] args) 
	{
		Vibrate vibrateFrame = new Vibrate();
		vibrateFrame.setVibrateStrength(10);
	}
}
