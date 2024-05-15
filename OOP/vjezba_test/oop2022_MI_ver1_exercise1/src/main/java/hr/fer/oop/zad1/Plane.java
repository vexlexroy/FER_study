/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.zad1;

/**
 *
 * @author vexlexroy
 */
class Plane extends Aircraft {
    private int capacity=0;
    private int[] motorsStatus;
    
    public Plane(String m, String d, int capcaity, int[]status) {
        super(m, d);
        this.capacity=capcaity;
        this.motorsStatus=status;
    }
    
    
    public Status aircraftStatus(){
        int minimal=100;
        for(int i:motorsStatus){
            if(i<minimal)minimal=i;
        }
        if(minimal>80 && minimal<100) return Status.NEED_CHECK;
        if(minimal<80) return Status.OUT_OF_SERVICE;
        if(minimal == 100) return Status.FUNCTIONAL;
        
        return null;
    }
    
    public String toString(){
        return "Aircraft model "+this.getModel()+" is produced "+this.getDateProduced()+" and has "+this.motorsStatus.length+" motors and capacity of "+this.capacity+".";
    }

    public int getCapacity() {
        return capacity;
    }

    public int[] getMotorsStatus() {
        return motorsStatus;
    }

    public void setMotorsStatus(int[] motorsStatus) {
        this.motorsStatus = motorsStatus;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    
}
