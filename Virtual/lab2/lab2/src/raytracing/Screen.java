package raytracing;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * Klasa predstavlja ekran kroz koji se 'gleda' scena kod modela crtanja slike
 * pomocu ray tracinga. Ekran je kvadratnog oblika, a definiran je velicinom
 * stranice i rezolucijom (broj piksela po duzini). Smjesten je u x-y ravninu
 * tako da mu se centar nalazi u sredistu tog trodimenzionalnog koordinatnog
 * sustava.
 * <p>Copyright: Copyright (c) 2003</p>
 * @author Milenka Gadze, Miran Mosmondor
 * @version 1.1
 */

import java.awt.*;
import javax.swing.*;
import java.awt.geom.*;

 public class Screen {

  private double size;
  private int resolution;
  private int i=0, j=0;

  /**
   * Glavni konstruktor koji postavlja velicinu i rezoluciju ekrana.
   *
   * @param size velicina stranice ekrana
   * @param resolution rezolucija ekrana
   */
  public Screen(double size, int resolution) {
    this.size=size;
    this.resolution=resolution;
  }

  /**
   * Metoda koja za svaki piksel slike (definiran parom varijabli i,j) vraca
   * tocku na ekranu.
   *
   * @param i indeks stupca u kojem se nalazi piksel
   * @param j indeks retka u kojem se nalazi piksel
   * @return koordinate piksela u virtualnom prostoru
   */
  public Point getPoint(int i, int j) {
	  double x = ((double)i - (double)resolution / 2) / ((double)resolution / size);
      double y = ((double)j - (double)resolution / 2) / ((double)resolution / size);
      Point p = new Point(x, y, 0);
      return p;
  }
}