package Week05;

class Song {
	private String title;
	
	public Song(String title) {
		this.title = title;
	}
	public String getTitle() {
		return this.title;
	}	
}
public class A03_Pract_Song {
	public static void main(String[] args) {
		Song mySong = new Song("Nessun Dorma");
		Song yourSong = new Song("���ִ� �� �� �̷��");
		System.out.println("�� �뷡�� " + mySong.getTitle());
		System.out.println("�� �뷡�� "+ yourSong.getTitle());
	}
}







