package com.data.Queue;

import java.util.LinkedList;
import java.util.Queue;

// Cola (Queue) => FIFO (First In First Out)

// Por defecto java incluye una clase LinkedList que implementa la interfaz de cola
// Esta clase contiene los métodos más comunes para trabajar con una cola

// add()    -> Agrega un elemento a la cola
// poll()   -> Elimina el primer elemento de la cola
// peek()   -> Obtiene el primer elemento de la cola sin eliminarlo
// size()   -> Obtiene el tamaño de la cola
// isEmpty()  -> Verifica si la cola está vacía

public class QueueExample {

    public static void main(String[] args) {
        // manualQueue(args);
        autoQueue(args);
    }

    public static void manualQueue(String[] args) {
        Queue<String> cola = new LinkedList<>();

        // Agregar elementos a la cola
        cola.add("Hola");
        cola.add("Mundo");
        cola.add("!");

        // Acceder y eliminar el primer elemento de la cola
        String primerElemento = cola.poll();
        System.out.println(primerElemento); // Salida: Hola

        // Acceder al primer elemento sin eliminarlo de la cola
        String primerElementoSinEliminar = cola.peek();
        System.out.println(primerElementoSinEliminar); // Salida: Mundo

        for (String elemento : cola) {
            System.out.println(elemento);
        }
    }

    public static void autoQueue(String[] args) {

        Queue<Integer> cola = new LinkedList<>();

        for (int i = 0; i < 5; i++) {
            cola.add(i);
        }

        while (!cola.isEmpty()) {
            cola.poll();
            System.out.println(cola);
        }
    }

}
