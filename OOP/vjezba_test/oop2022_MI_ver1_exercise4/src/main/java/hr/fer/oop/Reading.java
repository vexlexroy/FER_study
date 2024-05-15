/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hr.fer.oop;
import java.time.LocalDate;

/**
 *
 * @author vexlexroy
 */
class Reading {
    private Integer deviceId;
    private SensorReadingValue[] sensorReadings;
   private LocalDate timestamp;

    public void setDeviceId(Integer deviceId) {
        this.deviceId = deviceId;
    }

    public void setSensorReadings(SensorReadingValue[] sensorReadings) {
        this.sensorReadings = sensorReadings;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }

    public Integer getDeviceId() {
        return deviceId;
    }

    public SensorReadingValue[] getSensorReadings() {
        return sensorReadings;
    }

    public LocalDate getTimestamp() {
        return timestamp;
    }
   
   
    
}
