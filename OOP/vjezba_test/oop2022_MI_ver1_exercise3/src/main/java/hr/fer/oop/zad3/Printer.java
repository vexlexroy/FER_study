/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.zad3;

/**
 *
 * @author vexlexroy
 */
public class Printer {
    
    public static String printAudioList(MyList<? extends Audio> x){
        StringBuilder sb= new StringBuilder();
        for(int i=0;i<x.size();i++){
            sb.append(x.elementAt(i).getTitle()+" - ");
            sb.append(x.elementAt(i).getLength()+" sec. - ");
            sb.append(x.elementAt(i).getCodec()+"\n");
        }
        return sb.toString();
    }
    
    public static String printVideoList(MyList<Video> x){
        StringBuilder sb= new StringBuilder();
        for(int i=0;i<x.size();i++){
            sb.append(x.elementAt(i).getTitle()+" - ");
            sb.append(x.elementAt(i).getLength()+" sec. - ");
            sb.append(x.elementAt(i).getFormat()+"\n");
        }
        return sb.toString();
    }
    
}
