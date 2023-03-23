package com.data.LinkedList;

import java.util.List;
import java.util.LinkedList;

import com.data.Persona;

// En las listas enlazadas no hay posiciones fijas, por lo que no se pueden obtener datos en especifico
// para llegar a un determinado elemento se debe recorrer todos los datos anteriores

public class MyLinkedList {

    public static void main(String[] args) {

        List<Persona> lista = new LinkedList<Persona>();

        // .add() agrega elementos a la linkedList

        // Al Final (Forma tradicional)
        lista.add(new Persona(1, "Juan", 30));
        lista.add(new Persona(2, "Pedro", 31));
        lista.add(new Persona(3, "Diego", 32));
        lista.add(new Persona(4, "Hassan", 33));

        // Al comienzo
        lista.add(0, new Persona(5, "Test", 99));

        for (Persona persona : lista) {
            System.out.println("name: " + persona.getName());
        }

        // .remove() para eliminar elementos

        // Borrar un elemento donde el nombre sea Diego

        String nameToRemove = "Diego";

        for (Persona persona : lista) {
            if (persona.getName().equals(nameToRemove)) {
                lista.remove(persona);
                break;
            }
        }

        // .size() para obtener longitud de un arrayList
        lista.size(); // retornará 4

        // .getFirst -> El primer elemento, sin toString() retorna dirección de memoria!
        // .getLast -> El ultimo elemento, sin toString() retorna dirección de memoria!

        // .clear() -> Limpia la lista por completo

        // .isEmpty() -> retorna booleano dependiendo si está vacia o no

    }
}
