package raytracing;

/**
 * <p>Title: Scene</p>
 * <p>Description: </p>
 * Klasa predstvlja scenu kod modela crtanja slike pomocu ray tracinga. Sastoji
 * se od izvora svjetlosti i konacnog broja objekata.
 * <p>Copyright: Copyright (c) 2003</p>
 * @author Milenka Gadze, Miran Mosmondor
 * @version 1.1
 */

import java.awt.*;
import javax.swing.*;
import java.awt.geom.*;
import java.awt.event.*;

public class Scene {

  final int MAXDEPTH=5; //maksimalna dubina rekurzije
  private int numberOfObjects;
  private Sphere[] sphere;
  private Point lightPosition;
  private ColorVector backroundColors=new ColorVector(0, 0, 0);
  private ColorVector light=new ColorVector((float)1 , (float)1,(float)1);
  private ColorVector ambientLight=new ColorVector((float)0.5, (float)0.5, (float)0.5);

  /**
   * Inicijalni konstruktor koji postavlja poziciju svijetla i parametre svih
   * objekata u sceni.
   *
   * @param lightPosition pozicija svijetla
   * @param numberOfObjects broj objekata u sceni
   * @param sphereParameters parametri svih kugli
   */
  public Scene(Point lightPosition, int numberOfObjects, SphereParameters[] sphereParameters) {
    this.lightPosition=lightPosition;
    this.numberOfObjects=numberOfObjects;
    sphere=new Sphere[numberOfObjects];
    for (int i=0; i<numberOfObjects; i++) {
      sphere[i]=new Sphere(sphereParameters[i]);
    }
  }

  /**
   * Metoda provjerava da li postoji sjena na tocki presjeka. Vraca true ako
   * se zraka od mjesta presjeka prema izvoru svjetlosti sjece s nekim objektom.
   *
   * @param intersection tocka presjeka
   * @return true ako postoji sjena u tocki presjeka, false ako ne postoji
   */
  private boolean shadow(Point intersection) {
    return false;
  }

  /**
   * Metoda koja pomocu pracenja zrake racuna boju u tocki presjeka. Racuna se
   * osvjetljenje u tocki presjeka te se zbraja s doprinosima osvjetljenja koje
   * donosi reflektirana i refraktirana zraka.
   *
   * @param ray pracena zraka
   * @param depth dubina rekurzije
   * @return vektor boje u tocki presjeka
   */
  public ColorVector traceRay(Ray ray, int depth) {
    return null;
  }
}