package Cuentas;

// import Cuentas.Cuenta;  // Importa la clase Cuenta, si no fuese del mismo paquete

public class Actividad01 {

    public static void main(String[] args) {

        Cuenta cuenta_1 = new Cuenta();

        // System.out.println(cuenta_1.getSaldo()); // imprime 0

        cuenta_1.setSaldo(100);

        System.out.println(cuenta_1.getSaldo()); // imprime 100
    }
}
