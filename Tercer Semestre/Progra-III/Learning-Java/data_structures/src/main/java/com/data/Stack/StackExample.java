package com.data.Stack;

import java.util.Stack;

// Pila (Stack) => LIFO (Last In First Out)

// Por defecto java incluye una clase Stack que implementa la interfaz de pila
// Esta clase contiene los métodos más comunes para trabajar con una pila

// push()  -> Agrega un elemento a la pila
// pop()   -> Elimina el elemento superior de la pila
// peek()  -> Obtiene el elemento superior de la pila sin eliminarlo
// empty() -> Verifica si la pila está vacía

// | 3 |--- pila.pop() -->|   |------------------|   |------------------|  |------------------|
// | 2 |------------------| 2 |--- pila.pop() -->|   |------------------|  |------------------|
// | 1 |------------------| 1 |------------------| 1 |--- pila.pop() -->|  |------------------|
// --------------------------------------------------------------------------------------------

// |======> pila.pop() ==> (3)

public class StackExample {
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
