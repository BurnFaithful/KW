package Game;

public class Main {
	
	public static final int WINDOW_SIZE_WIDTH = 1024;
	public static final int WINDOW_SIZE_HEIGHT = 768;
	
	
	public static void main(String[] args) {
		
		MainGame mainGame = new MainGame();
		
		mainGame.Init();
		
		mainGame.Update();
	}
}
