package vsta;

import excepciones.DNIException;
import excepciones.MatriculaException;
import modelo.Vehiculo;

public class Main {
    public static void main(String[] args) {
        try {
            Vehiculo v1=new Vehiculo("Juan", "Lopez", "32088831J", "4502POL"); 
            System.out.println(v1);
        } catch (DNIException | MatriculaException e) {
            System.out.println(e.getMessage());
        }
    }
}
