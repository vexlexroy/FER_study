/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.zad3;

/**
 *
 * @author vexlexroy
 */
public class MediaPrinter<E extends Media> extends PrintableList{

    @Override
    public String print() {
        StringBuilder sb = new StringBuilder();
        Media x;
       for(int i=0;i<this.size();i++){
           x=(Media) this.elementAt(i);
         sb.append(x.getTitle()+" is ");
         sb.append(x.getLength()+" seconds long.\n");
       }
       return sb.toString();
    }
    
}
