/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.mtexam.task2;

import java.util.Random;

/**
 *
 * @author vexlexroy
 */
class MobileAgent extends Agent implements Movable {
    private int taskId=1;

    public MobileAgent(String name, int ID) {
        super(name, ID);
    }

    public void doRemoteTask(){
        taskId=(int)(Math.random()*10)+1;
    }
    
    @Override
    public String getAgentType() {
        return "mobile agent";
    }

    public int getTaskId() {
        return taskId;
    }
    
    
    
    
}
