package modelo;

public class DatosVehiculo {
    Vehiculo vehiculo;
    Long entrada;
    Long salida;
    Long tiempoEspera;
    public DatosVehiculo(Vehiculo vehiculo) {
        this.vehiculo = vehiculo;
        this.entrada=Reloj.ahora();
    }
    public Vehiculo getVehiculo() {
        return vehiculo;
    }
    public long getTiempoEspera() {

        return (salida-entrada)/1000;
    }
    public void atiende(){
        this.salida=Reloj.ahora();
        tiempoEspera= salida-entrada;
        System.out.println("Tiempo total de espera:"+tiempoEspera+"ms");

    }


}
