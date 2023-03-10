package com.data.Exceptions;

public class Exceptions {
    public static void main(String[] args) {
        zeroDivisionError();
    }

    public static void zeroDivisionError() {

        int res;

        try {
            res = 3 / 0;
        } catch (Exception e) {
            System.out.println("División indefinida en 0");
        }
    }

    public static void outIndex() {

        int edades[] = { 1, 2, 3, 4 };

        try {
            System.out.println("la edad es: " + edades[4]);
        } catch (Exception e) {
            System.out.println("Out of index");
        }
    }
}