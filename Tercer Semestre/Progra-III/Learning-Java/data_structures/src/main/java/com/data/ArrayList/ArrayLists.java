package com.data.ArrayList;

import java.util.List;
import com.data.Persona;
import java.util.ArrayList;

public class ArrayLists {

    public static void main(String[] args) {

        List<Persona> lista = new ArrayList<Persona>();

        // .add() agrega elementos
        lista.add(new Persona(1, "Juan", 30));
        lista.add(new Persona(2, "Pedro", 31));
        lista.add(new Persona(3, "Diego", 32));
        lista.add(new Persona(4, "Hassan", 33));

        // Recorrer por indice
        for (int i = 0; i < lista.size(); i++) {
            System.out.println("name: " + lista.get(i).getName());
        }

        // remove() elimina elementos (en arrayList borra por indice)
        lista.remove(0); // borrará a Persona(1, "Juan", 30)

        // .size() para obtener longitud de un arrayList
        lista.size(); // retornará 4

        // .clear() -> Limpia la lista por completo

        // .isEmpty() -> retorna booleano dependiendo si está vacia o no
    }
}
