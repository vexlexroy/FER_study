package raytracing;

/**
 * <p>Title: Sphere</p>
 * <p>Description: </p>
 * Klasa predstavlja kuglu u prostoru. Nasljeduje apstraktnu klasu Object. Kugla
 * je odredena svojim polozajem, radijusom, bojom, parametrima materijala i
 * udjelima pojedninih zraka (osnovne, odbijene i lomljene).
 * <p>Copyright: Copyright (c) 2003</p>
 * @author Milenka Gadze, Miran Mosmondor
 * @version 1.1
 */


import java.awt.*;
import javax.swing.*;
import java.awt.geom.*;
import java.awt.event.*;

public class Sphere extends Object{

  private double radius;
  final double Epsilon = 0.0001;
  private double rayDistanceFromCenter;
  private Point IntersectionPoint;

  /**
   * Inicijalni konstruktor koji postavlja sve parametre kugle. Za prijenos
   * parametara koristi se pomocna klasa SphereParameters.
   *
   * @param sphereParameters parametri kugle
   */
  public Sphere(SphereParameters sphereParameters) {
    super(sphereParameters.getCenterPosition(), sphereParameters.getRaysContributions(), sphereParameters.getMaterialParameters(),sphereParameters.getN(), sphereParameters.getNi());
    this.radius=sphereParameters.getRadius();
  }

  /**
   * Metoda ispituje postojanje presjeka zrake ray s kuglom. Ako postoji presjek
   * postavlja tocku presjeka IntersectionPoint, te
   * vraca logicku vrijednost true.
   *
   * @param ray zraka za koju se ispituje postojanje presjeka sa kuglom
   * @return logicku vrijednost postojanja presjeka zrake s kuglom
   */
  public boolean intersection(Ray ray) {
    return false;
  }

  /**
   * Vraca tocku presjeka kugle sa zrakom koja je bliza pocetnoj tocki zrake.
   *
   * @return tocka presjeka zrake s kuglom koja je bliza izvoru zrake
   */
  public Point getIntersectionPoint() {
    return IntersectionPoint;
  }

  /**
	* Vraca normalu na kugli u tocki point
	*
	* @param point na kojoj se racuna normala na kugli
	* @return normal vektor normale
	*/
  public Vector getNormal(Point point) {
	return null;
  }


}