package z1;

class PlayedGame extends Game implements PlaybleGame {
	
	int highScore=0;
	int numberOfPlays=0;
	

	public PlayedGame(String name, String platform) {
		super(name, platform);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void play(int highScore) {
		this.numberOfPlays++;
		if(this.highScore<highScore) {
			this.highScore=highScore;
		}
		
	}

	@Override
	public int getNumberOfPlays() {
		return this.numberOfPlays;
	}

	@Override
	public int getHighScore() {
		return this.highScore;
	}
	
	@Override
	public String toString() {
		return ("PlayedGame [name="+this.getName()+", platform="+this.getPlatform()+", numberOfPlays="+this.numberOfPlays+", highhighScore="+this.highScore+"]");
	}

}
