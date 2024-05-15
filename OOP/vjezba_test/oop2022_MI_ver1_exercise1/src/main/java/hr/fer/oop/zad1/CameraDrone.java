/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.zad1;

/**
 *
 * @author vexlexroy
 */
class CameraDrone extends Aircraft implements Unmanned{
    private final int range;
    private int[] qualities;

    public CameraDrone(String m, String d, int range, int[] quality) {
        super(m, d);
        this.range=range;
        this.qualities=quality;
    }

    @Override
    public Status aircraftStatus() {
        int sum=0;
        float avg=0;
        for(int i:qualities){
            sum=sum+i;
        }
        avg = (float)sum/qualities.length;
        if(avg>70 && avg <=100) return Status.FUNCTIONAL;
        else if(avg>=0 && avg <50)   return Status.OUT_OF_SERVICE;
        else if(avg>=50 && avg <=70) return Status.NEED_CHECK;
        else return null;
    }
    @Override
        public String toString(){    
        return "Aircraft model "+this.getModel()+" is produced "+this.getDateProduced()+" and has "+this.qualities.length+" elements.";  
        }

    @Override
    public double coverArea(Number height) {
        
        return (double)height*this.range;
    }

    public int[] getQualities() {
        return qualities;
    }

    public int getRange() {
        return range;
    }

    public void setQualities(int[] qualities) {
        this.qualities = qualities;
    }
    
    
}
