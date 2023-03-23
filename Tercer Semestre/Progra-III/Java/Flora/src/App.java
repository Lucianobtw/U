public class App {
    public static void main(String[] args) throws Exception {

        Arbol arbol_1 = new Arbol(1, "Pino", 2.10, true, "templado", "Cipres");
        Arbusto arbus_1 = new Arbusto(2, "Jazmin", 1.00, true, "templado", "Arbusto", 0.70);
        Planta planta_1 = new Flor(3, "Rosa", 1.0, true, "templado", "Rosa blanca");

        arbol_1.name();
        arbus_1.name();
        planta_1.name();
    }
}
