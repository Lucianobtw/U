import Stack.MyStack;

public class App {
    public static void main(String[] args) throws Exception {

        useStack();
    }

    public static void useStack() {
        MyStack pila = new MyStack(5);

        for (int i = 1; i <= 10; i++) {
            pila.push(i);
        }

        System.out.println("Pila después de agregar elementos: " + pila.toString());

        while (!pila.isEmpty()) {
            int elementoEliminado = pila.pop();
            System.out.println("Elemento eliminado de la pila: " + elementoEliminado);
            System.out.println("Pila después de eliminar elemento: " + pila.toString());
        }
    }
}
