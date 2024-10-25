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
import java.util.concurrent.CancellationException;
import java.awt.event.*;

public class Scene {

  final int MAXDEPTH=5; //maksimalna dubina rekurzije
  private int numberOfObjects;
  private Sphere[] sphere;
  private Point lightPosition;
  private ColorVector backroundColors=new ColorVector(0, 0, 0);
  private ColorVector light=new ColorVector(1,1,1);
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
	Ray shadowR = new Ray(intersection, lightPosition);
	for(Sphere sph: this.sphere) {
		if(sph.intersection(shadowR)) {
			return true;
		}
	}
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
	Point last = null; 
	Sphere lastsph = null;
	ColorVector colorV = backroundColors;
	if (depth>MAXDEPTH) {colorV.correct(); return colorV;}
	for(Sphere sph:sphere) {
		if(sph.intersection(ray)) {
			//colorV = new ColorVector(0.5f , 1 , 1);
			if(last == null) {
				
				last=sph.getIntersectionPoint();
				lastsph=sph;
			}
			else {
				Point origin = ray.getStartingPoint();
				Point hit = sph.getIntersectionPoint();
				double distn = (new Vector(origin, hit).getLength());
				double distl = (new Vector(origin, last).getLength());
				if(distl>distn) { // trazi najblizu kuglu i sprema ju ako je bliza od prosle
					last=hit;
					lastsph=sph;
				}
			}	
		}
	}
	if(lastsph!=null) {
//		System.out.println("hit");
		PropertyVector ambiK = lastsph.getKa();
		PropertyVector difK = lastsph.getKd();
		PropertyVector specK = lastsph.getKs();
		float shine = lastsph.getN();
		Vector N = lastsph.getNormal(last);
		Vector L = new Vector(last, lightPosition);
		Vector R = L.getReflectedVector(N);
		Vector V = new Vector(last, ray.getStartingPoint());
		Vector Re = L.getRefractedVector(R, lastsph.getNi());
		N.normalize(); L.normalize(); R.normalize(); V.normalize(); Re.normalize();
		float Ar = (ambiK.getRedParameter()*ambientLight.getRed());
		float Ag = (ambiK.getGreenParameter()*ambientLight.getGreen());
		float Ab = (ambiK.getBlueParameter()*ambientLight.getBlue());
		float LN = (float)L.dotProduct(N);
		float Dr =(difK.getRedParameter()*light.getRed()*LN);
		float Dg =(difK.getGreenParameter()*light.getGreen()*LN);
		float Db =(difK.getBlueParameter()*light.getBlue()*LN);
		float RV = (float)R.dotProduct(V);
		float Sr =(specK.getRedParameter()*light.getRed()* (float) Math.pow(RV, shine));
		float Sg =(specK.getGreenParameter()*light.getGreen()*(float) Math.pow(RV, shine));
		float Sb =(specK.getBlueParameter()*light.getBlue()*(float) Math.pow(RV, shine));
		ColorVector colorA=new ColorVector(Ar, Ag, Ab);
		ColorVector colorD=new ColorVector(Dr, Dg, Db);
		ColorVector colorS=new ColorVector(Sr, Sg, Sb);
		colorA.correct();
		colorD.correct();
		colorS.correct();
		if(shadow(last)) {
			System.out.println("yes Shadow");
			colorV = colorA;
		}
		else {
			colorV = colorA.add(colorD).add(colorS);
		}
		colorV.correct();
		Ray next_ref = new Ray(last,R);
		Ray next_rif = new Ray(last,Re);
		// vraca colorV i dodaje sljedece zrake s umnoskom faktora refleksije i refrakcije od pojedine kugle
	    colorV.add(traceRay(next_ref, depth+1).multiple(lastsph.getReflectionFactor())).add(traceRay(next_rif, depth+1).multiple(lastsph.getRefractionFactor()));
	    colorV.correct();
	    return colorV;
	}
	colorV.correct();
    return colorV;
  }
}