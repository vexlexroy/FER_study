/*
 */
package hr.fer.oop.mtexam.task2;

/**
 *
 * @author vexlexroy
 */
abstract class Agent {
    private final String name;
    private final int ID;

     Agent(String name, int ID) {
        this.name = name;
        this.ID = ID;
    }

    public int getID() {
        return ID;
    }

    public String getName() {
        return name;
    }

    /*public void setID(int ID) {
        this.ID = ID;
    }*/

   /* public void setName(String name) {
        this.name = name;
    }*/

    @Override
    public String toString() {
        return "(name: "+name+", id: "+ID+")";
    }
    
    public abstract String getAgentType();
    
    
    
    
}
