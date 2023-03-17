package Stack;

import java.util.Stack;

public class JavaStack {

    public static void main(String[] args) {

        // manualStack(args);
        autoStack(args);
    }

    public static void manualStack(String[] args) {

        // Crear una pila vacía
        Stack<Integer> pila = new Stack<>();

        // Agregar elementos a la pila
        pila.push(1);
        pila.push(2);
        pila.push(3);

        // Obtener el elemento superior de la pila sin eliminarlo
        int elementoSuperior = pila.peek();
        System.out.println("Elemento superior de la pila: " + elementoSuperior);

        // Eliminar el elemento superior de la pila
        int elementoEliminado = pila.pop();
        System.out.println("Elemento eliminado de la pila: " + elementoEliminado);
    }

    // <--------------------------------------------------------------------------------------->

    public static void autoStack(String[] args) {

        Stack<Integer> pila = new Stack<>();

        // Agregar elementos a la pila del 1 al 5
        for (int i = 1; i <= 5; i++) {
            pila.push(i);
        }

        // Imprimir la pila
        System.out.println("Pila después de agregar elementos: " + pila);

        // Eliminar elementos de la pila con un ciclo while
        while (!pila.isEmpty()) {
            int elementoEliminado = pila.pop();
            System.out.println("Elemento eliminado de la pila: " + elementoEliminado);
            System.out.println("Pila después de eliminar elemento: " + pila);
        }
    }

}
