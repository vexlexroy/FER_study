package z1;

public class Main {

	public static void main(String[] args) {
	    PlayedGame game = new PlayedGame("Doom", "PC");

	    game.play(1500);
	    game.getNumberOfPlays(); // vraca 1
	    game.getHighScore(); // vraca 1500

	    for (int i = 0; i < 20; i++) {
	        game.play(1000);
	    }
	    game.getNumberOfPlays(); // vraca 21
	    game.getHighScore(); // vraca 1500

	    game.play(2000);
	    game.getNumberOfPlays(); // vraca 22
	    game.getHighScore(); // vraca 2000

	    System.out.println(game); // ispisuje "PlayedGame [name=Doom, platform=PC, numberOfPlays=22, highScore=2000]"

	}

}
