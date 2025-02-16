package modelo;

import excepciones.DNIException;
import excepciones.MatriculaException;

public class Vehiculo {
 private String nombre;
 private String apellidos;
 private String dni;
 private String matricula;
 private String identificador;
public Vehiculo(String nombre, String apellidos, String dni, String matricula) throws DNIException, MatriculaException {
    this.nombre =nombre;
    this.apellidos = apellidos;
    this.dni = dni;
    this.matricula = matricula;
    
    setIdentificador(matricula, nombre, apellidos, dni);
    setDni(dni);
    setMatricula(matricula);
    
}
public String getNombre() {
    return nombre;
}
public void setNombre(String nombre) {
    this.nombre = nombre;

}
public String getApellidos() {
    return apellidos;
}
public void setApellidos(String apellidos) {
    this.apellidos = apellidos;
}
public String getDni(){
    
    return dni;
}
public void setDni(String dni) throws DNIException {
    if (dni.length() != 9) {
        throw new DNIException();
    }
    // variables
    String letras = "T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E";
    String[] letrasEnDni = letras.split(",");
    boolean iguales = false;
    // Sacar numero
    String numero = dni.substring(0, (dni.length() - 1));
    int numeroDni=0;
    try {
         numeroDni = Integer.parseInt(numero);
    } catch (NumberFormatException e) {
        e.getMessage();
    }
    int posicionLetraDNi = numeroDni % 23;
    // sacar la letra
    String letra = dni.substring(8).toUpperCase();
    char letraBuscar = letra.charAt(0);
    // buscar y comparar
    if (letrasEnDni[posicionLetraDNi].charAt(0) == letraBuscar) {
        iguales = true;
    }
    if (!iguales) {
        throw new DNIException();
    }
    this.dni = dni;
 
 }
  
 
 public String getMatricula() {
    return matricula;
}
public void setMatricula(String matricula) throws MatriculaException {

    if (!matricula.matches("\\d{4}[A-Z]{3}")) {
        throw new MatriculaException();
    }

        this.matricula = matricula;
    }
    public static boolean isValidString(String str) {
        
        String alfabeto2= "abcdefghijklmnopqrstuvwxyzñABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
        return str.matches(alfabeto2);
    }
    public String getIdentificador() {
    return identificador;
}

public void setIdentificador(String identificador, String nombre, String apellidos, String dni) {
    identificador="";
    identificador+=nombre.substring(0, 1);
    identificador+=apellidos.substring(0, 1);
    identificador+=dni.substring((dni.length()-4), (dni.length()-1));


    this.identificador = identificador;

}
@Override
public String toString() {
    return "Vehiculo [nombre=" + nombre + ", apellidos=" + apellidos + ", dni=" + dni + ", matricula=" + matricula
            + ", identificador=" +identificador + "]";
}

}
