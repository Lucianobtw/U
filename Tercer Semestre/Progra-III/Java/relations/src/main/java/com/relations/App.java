package com.relations;

import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) {

        Auto car_1 = new Auto();

        car_1.setId(1L);
        car_1.setMarca("Mercedez");
        car_1.setModelo("GullWing");

        List<Propietario> ownersArray = new ArrayList<Propietario>();

        Propietario owner_1 = new Propietario(1, "Pedro");
        Propietario owner_2 = new Propietario(2, "Jose");

        ownersArray.add(owner_1);
        ownersArray.add(owner_2);

        car_1.setOwnerList(ownersArray);
    }
}
