package z2;

class HealthVaccinationCenter extends HealthCenter implements VaccinationCenter{
	private int numberOfPatients;
	private int vaccinatedPatients=0;
	

	public HealthVaccinationCenter(String name, String address, int registeredPatients) {
		super(name, address, registeredPatients);
		this.numberOfPatients=registeredPatients;
	}

	@Override
	public void vaccinate(int numberOfPatients) {
		this.vaccinatedPatients+=numberOfPatients;
		if(numberOfPatients<=this.numberOfPatients)
		this.numberOfPatients=this.numberOfPatients-numberOfPatients;
		else
		this.numberOfPatients=0;
		
	}

	@Override
	public int getVaccinatedPatients() {
		return this.vaccinatedPatients;
	}

	@Override
	public int getNotVaccinatedPatients() {
		return this.numberOfPatients;
	}
	
	@Override
	public String toString() {
		return "HealthVaccinationCenter [name="+ getName() +", address="+getAddress()+", registered patients="+getRegisteredPatients()+", vaccinated patients="+getVaccinatedPatients()+"]";
	}

}
