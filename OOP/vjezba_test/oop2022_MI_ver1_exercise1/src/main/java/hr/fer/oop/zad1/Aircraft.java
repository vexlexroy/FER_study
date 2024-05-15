package hr.fer.oop.zad1;

// add and fix everything except toString method

abstract class Aircraft {
   private final String model;
   private final String dateProduced;

    public Aircraft(String m,String d) {
    this.model=m;
    this.dateProduced=d;
    }
    
    public abstract Status aircraftStatus();
   

	@Override
	public String toString() {
		return String.format("Aircraft model %s is produced %s", model, dateProduced);
	}

    public String getDateProduced() {
        return dateProduced;
    }

    public String getModel() {
        return model;
    }

    /*public void setDateProduced(String dateProduced) {
        this.dateProduced = dateProduced;
    }

    public void setModel(String model) {
        this.model = model;
    }*/
        	
}

