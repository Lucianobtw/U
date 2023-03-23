package com.convertions;

public class Conversiones {

    public static void main(String[] args) {

        // converINTS();
        // converSTR();
        // convertToStr();

    }

    public static void converINTS() {
        double num = 1.67;

        // casting to int
        int numInt = (int) num;

        // casting to long
        long numLong = (long) num;

        System.out.println("double: " + num);
        System.out.println("int: " + numInt);
        System.out.println("long: " + numLong);
    }

    public static void converSTR() {

        String cantidas = "15";
        String precio = "150.27";

        int cantInteger = Integer.parseInt(cantidas);
        double precioDouble = Double.parseDouble(precio);

        double total = (cantInteger * precioDouble);
        System.out.println("Total: " + total);
    }

    public static void convertToStr() {

        int age = 10;
        double height = 1.89;

        String edadStr = String.valueOf(age);
        String heightStr = String.valueOf(height);

        System.out.println(edadStr + " " + heightStr);

    }

}
