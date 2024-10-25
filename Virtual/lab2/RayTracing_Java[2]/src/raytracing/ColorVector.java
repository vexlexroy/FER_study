package raytracing;

/**
 * <p>Title: Colors</p>
 * <p>Description: </p>
 * Pomocna klasa koja predstavlja vektor boje. Boja je odredena s tri komponente :
 * crvenom, zelenom i plavom. Svaka komponenta odredena je decimalnim brojem
 * od 0 do 1. Koristi se kod odredivanja boje pomocu intenziteta.
 * <p>Copyright: Copyright (c) 2003</p>
 * @author Milenka Gadze, Miran Mosmondor
 * @version 1.1
 */

public class ColorVector {

  private float red, green, blue;

  /**
   * Inicijalni konstruktor koji postavlja vrijednost crvene, zelene i plave
   * komponente boje.
   *
   * @param red crvena komponenta boje
   * @param green zelena komponenta boje
   * @param blue plava komponenta boje
   */
  public ColorVector(float red, float green, float blue) {
    this.red=red;
    this.green=green;
    this.blue=blue;
  }

  /**
   * Vraca crvenu komponentu boje.
   *
   * @return crvena komponenta boje
   */
  public float getRed() {
    return red;
  }

  /**
   * Vraca zelenu komponentu boje.
   *
   * @return zelena komponenta boje
   */
  public float getGreen() {
    return green;
  }

  /**
   * Vraca plavu komponentu boje.
   *
   * @return plava komponenta boje
   */
  public float getBlue() {
    return blue;
  }

  /**
   * Sluzi za zbrajanje dviju boja.
   *
   * @param c boja s kojom se zbraja
   * @return zbroj boja
   */
  public ColorVector add(ColorVector c) {
    return new ColorVector(red+c.getRed(),green+c.getGreen(),blue+c.getBlue());
  }

  /**
   * Sluzi za mnozenje komponenata boje skalarom.
   *
   * @param factor skalar s kojim se mnoze parametri boja
   * @return umnozak boje i skalara
   */
  public ColorVector multiple(double factor) {
    return new ColorVector((float)factor*red, (float)factor*green, (float)factor*blue);
  }

  /**
   * Sluzi za mnozenje komponenata dviju boja.
   *
   * @param c vektor boje s kojim se mnozi
   * @return umnozak dviju boja
   */
  public ColorVector multiple(ColorVector c) {
    return new ColorVector(c.getRed()*red, c.getGreen()*green, c.getBlue()*blue);
  }

  /**
   * Sluzi za mnozenje vektora boje s vektorom koeficijenata. Koristi se kod
   * odredivanja boje lokalnog osvjetljenja.
   *
   * @param c vektor koeficijenata s kojim se mnozi
   * @return vektor boje koji je rezultat mnozenja vektora boje s vektorom koeficijenata
   */
  public ColorVector multiple(PropertyVector c) {
    return new ColorVector(c.getRedParameter()*red, c.getGreenParameter()*green, c.getBlueParameter()*blue);
  }

 /**
   *
   * Sluzi za provjeravanje i ispravljanje vektora boje s obzirom na dozvoljene
   * granice boja od 0 do 1. U slucaju da su granice premasene vrijednosti se
   * zaokruzuju na najvisu, odnosno najmanju.
   */

  public void correct(){
    red = Math.max(0, Math.min(1, red));
    green = Math.max(0, Math.min(1, green));
    blue = Math.max(0, Math.min(1, blue));
  }

}