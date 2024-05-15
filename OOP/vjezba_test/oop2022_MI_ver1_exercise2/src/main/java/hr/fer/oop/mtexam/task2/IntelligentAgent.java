/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop.mtexam.task2;

/**
 *
 * @author vexlexroy
 */
class IntelligentAgent extends Agent {
    private IntelligentAgentType type;

    public IntelligentAgent(String name, int ID, IntelligentAgentType type) {
        super(name, ID);
        this.type=type;
    }

    public IntelligentAgentType getType() {
        return type;
    }

    public void setType(IntelligentAgentType type) {
        this.type = type;
    }

    
    
    @Override
    public String getAgentType() {
        return "intelligent agent";
    }
    
}
