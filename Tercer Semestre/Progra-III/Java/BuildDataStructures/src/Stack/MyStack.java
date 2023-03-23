package Stack;

public class MyStack {
    private int maxSize; // tamaño maximo del array
    private int[] stackArray; // Array de enteros que almacenará los elementos
    private int top; // entero, guardará el indice del array donde se encuentre el top de la pila

    // Constructor, se inicializa la pila, con el tamaño/size se crea el array de
    // enteros
    // Al asignar top como -1 se intuye que la pila está vacía (al agregar un nuevo
    // elemento el indice será -1 + 1 = index 0)

    public MyStack(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    // Verificadores de estado (retornan Booleans)

    // Si el top = -1 significa que se encuentra como al inicializarse
    public boolean isEmpty() {
        return (top == -1);
    }

    // Verificación por índice
    // if maxSize = 9 entonces el maxIndex es 8 (maxSize - 1)
    public boolean isFull() {
        return (top == maxSize - 1);
    }

    // Método push() (agrega elementos a la Pila)
    // recibe un elemento a agregar (int) ...
    // verifica si la pila está llena de lo contrario incrementa el indice del top y
    // agrega el elemento en el top de la pila

    public void push(int element) {
        if (isFull()) {
            System.out.println("No puedes agregar más elementos a la pila");
        } else {
            top++;
            stackArray[top] = element;
        }
    }

    // Método pop()
    // Verifica el estado mediante isEmpty(), simbolicamente retorna un -1 haciendo
    // referencia al index vacio

    public int pop() {
        if (isEmpty()) {
            System.out.println("No puedes quitar elementos, la pila está vacia");
            return -1;
        } else {
            int value = stackArray[top];
            top--;
            return value;
        }
    }

    // Retorna el valor que se encuentra en la posición top

    public int peek() {
        if (isEmpty()) {
            System.out.println("La pila está vacía");
            return -1;
        } else {
            return stackArray[top];
        }
    }

    // crea una instancia de String, donde recorre el array y lo agrega a una cadena
    // de texto para representar la pila
    @Override
    public String toString() {

        StringBuilder sb = new StringBuilder();
        sb.append("[");

        for (int i = 0; i <= top; i++) {
            sb.append(stackArray[i]);
            if (i != top) {
                sb.append(", ");
            }
        }

        sb.append("]");
        return sb.toString();
    }
}