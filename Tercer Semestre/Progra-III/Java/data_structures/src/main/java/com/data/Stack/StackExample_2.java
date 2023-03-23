package com.data.Stack;

public class StackExample_2 {

    private int[] elementos;
    private int tope;

    public StackExample_2(int capacidad) {
        elementos = new int[capacidad];
        tope = -1;
    }

    public boolean estaVacia() {
        return tope == -1;
    }

    public boolean estaLlena() {
        return tope == elementos.length - 1;
    }

    public void apilar(int elemento) {
        if (estaLlena()) {
            throw new RuntimeException("La pila está llena");
        }
        tope++;
        elementos[tope] = elemento;
    }

    public int desapilar() {
        if (estaVacia()) {
            throw new RuntimeException("La pila está vacía");
        }
        int elementoDesapilado = elementos[tope];
        tope--;
        return elementoDesapilado;
    }

    public int cima() {
        if (estaVacia()) {
            throw new RuntimeException("La pila está vacía");
        }
        return elementos[tope];
    }

    public int tamanio() {
        return tope + 1;
    }

}
