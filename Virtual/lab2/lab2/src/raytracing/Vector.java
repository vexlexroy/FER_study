package raytracing;

/**
 * <p>Title: Vector</p>
 * <p>Description: </p>
 * Klasa predstavlja vektor u trodimenzionalnom prostoru.
 * <p>Copyright: Copyright (c) 2003</p>
 * @author Milenka Gadze, Miran Mosmondor
 * @version 1.1
 */

public class Vector {

  private double x,y,z;

  /**
   * Glavni konstruktor koji stvara vektor s komponentama x,y i z.
   *
   * @param x komponenta vektora
   * @param y komponenta vektora
   * @param z komponenta vektora
   */
  public Vector(double x, double y, double z) {
    this.x=x;
    this.y=y;
    this.z=z;
  }

  /**
   * Konstruktor koji stvara vektor odreden dvijema tockama. Tocka first
   * predstavlja hvatiste vektora, a tocka second vrh vektora.
   *
   * @param first tocka koja predstavlja pocetak, odnosno hvatiste vektora
   * @param second tocka koja zadaje vrh vektora
   */
  public Vector(Point first, Point second) {
//	System.out.println(first + "\n" + second);
    x=second.getX()-first.getX();
    y=second.getY()-first.getY();
    z=second.getZ()-first.getZ();
  }

  /**
   * Vraca x komponentu vektora.
   *
   * @return x komponenta vektora
   */
  public double getX() {
    return x;
  }

  /**
   * Vraca y komponentu vektora.
   *
   * @return y komponenta vektora
   */
  public double getY() {
    return y;
  }

  /**
   * Vraca z komponentu vektora.
   *
   * @return z komponenta vektora
   */
  public double getZ() {
    return z;
  }

  /**
   * Metoda normalizira vektor, odnosno stvara jedinicni vektor.
   */
  public void normalize() {
    double length=Math.sqrt(Math.pow(x,2)+Math.pow(y,2)+Math.pow(z,2));
    x/=length;
    y/=length;
    z/=length;
  }

  /**
   * Metoda vraca duzinu vektora.
   *
   * @return duzina vektora
   */
  public double getLength() {
    return Math.sqrt(Math.pow(x,2)+Math.pow(y,2)+Math.pow(z,2));
  }

  /**
   * Metoda sluzi za oduzimanje dva vektora.
   *
   * @param v vektor za koji se oduzima
   * @return vektor koji je jednak razlici
   */
  public Vector sub(Vector v) {
    return new Vector(x-v.getX(), y-v.getY(), z-v.getZ());
  }

  /**
   * Metoda sluzi za zbrajanje dva vektora.
   *
   * @param v vektor s kojim se zbraja
   * @return vektor koji je jednak zbroju
   */
  public Vector add(Vector v) {
    return new Vector(x+v.getX(), y+v.getY(), z+v.getZ());
  }

  /**
   * Metoda sluzi za mnozenje vektora skalarom.
   *
   * @param factor skalar s kojim se mnozi vektor
   * @return vektor koji je jednak umnosku vektora s skalarom
   */
  public Vector multiple(double factor) {
    return new Vector(x*factor, y*factor, z*factor);
  }

  /**
   * Koristi se za racunanje skalarnog produkta izmedu dva vektora.
   *
   * @param v vektor s kojim se racuna skalarni produkt
   * @return skalarni produkt dva vektora
   */
  public double dotProduct(Vector v) {
    return ((x*v.getX())+(y*v.getY())+(z*v.getZ()));
  }

  /**
   * Koristi se za racunanje vektorskog produkta.
   *
   * @param v vektor s kojim se racuna produkt
   * @return vektorski produkt dva vektora
   */
  public Vector crossProduct(Vector v) {
    double tx=(y*v.getZ())-(v.getY()*z);
    double ty=(z*v.getX())-(v.getZ()*x);
    double tz=(x*v.getY())-(v.getX()*y);
    return new Vector(tx, ty, tz);
  }

  /**
   * Metoda vraca kut u radijanima (od 0 do PI) izmedu doticnog vektora i
   * vektora v.
   *
   * @param v vektor na odnosu kojeg se odreduje kut
   * @return kut izmedu dva vektora (u radijanima od 0 do PI)
   */
  public double getAngle(Vector v) {
    return Math.acos(this.dotProduct(v)/(this.getLength()*v.getLength()));
  }

  /**
   * Vraca reflektirani vektor s obzirom na normalu.
   *
   * @param normal normala
   * @return reflektirani vektor
   */
  public Vector getReflectedVector(Vector normal) {
	  Vector R = normal.multiple(2 * this.dotProduct(normal)).sub(this);
      return R;
  }

  /**
   * Vraca refraktirani vektor s obzirom na normalu i indekse refrakcije
   * sredstva upadnog vektora i refraktiranog vektora.
   *
   * @param normal normala
   * @param nI indeks loma sredstva
   * @return refraktirani vektor
   */
  public Vector getRefractedVector(Vector normal, double nI) {
	  Vector U = this;
      Vector R;
      U.normalize();
      normal.normalize();
      double alfa = this.getAngle(normal);
      double cosA = Math.cos(alfa);
      double D = 4 * (Math.pow(nI * cosA, 2) - Math.pow(nI, 2) + 1);
      double a = (-2 * nI * cosA + Math.sqrt(D)) / 2;
      R = normal.multiple(-a).sub(U.multiple(nI));
      return R;  
  }

}