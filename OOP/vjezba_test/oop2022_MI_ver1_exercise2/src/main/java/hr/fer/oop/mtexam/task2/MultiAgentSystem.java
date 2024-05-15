/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.mtexam.task2;

/**
 *
 * @author vexlexroy
 */
class MultiAgentSystem {
   private static int generatedId=0;
   private Agent[] agents;
    public MultiAgentSystem(int num) {
        if(num<1)num=1;
        agents= new Agent[num];
    }
   public void addAgent(Agent agent){
       if(agent.getID()<agents.length)
        agents[agent.getID()]=agent;
    }
   public Agent[] getAgents(){
       return agents;
   }
   public static int generateId(){
       
       return MultiAgentSystem.generatedId++;
   }
   void printSystemInfo(){
       for(Agent x :agents){
           if(x!=null)
           System.out.println(x.getAgentType()+" "+x.toString());
       }
   }
   public int getNumberOfAgents(){
       int i=0;
    for(Agent x :agents){
           if(x!=null)
           i++;
       }  
    return i;
   }
    
}
