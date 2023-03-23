package com.data.BinaryTree;

public class Tree {

    private Node root; // Variable de instancia que representa la raíz del árbol.

    // Constructor que inicializa la raíz como null.
    public Tree() {
        root = null;
    }

    // Método público que permite insertar un nuevo node en el árbol.
    public void insert(int value) {
        Node newNode = new Node(value); // Crear un nuevo node con el valor recibido.
        root = insert(root, newNode); // Llamar al método privado insert para insertar el nuevo node.
    }

    // Método privado que inserta un nuevo node en el lugar correcto del árbol según
    // las reglas de un árbol binario de búsqueda.
    private Node insert(Node root, Node newNode) {
        if (root == null) { // Si el node raíz es null, el nuevo node se convierte en la raíz del árbol.
            root = newNode;
            return root;
        }
        if (newNode.value < root.value) { // Si el valor del nuevo node es menor que el valor del node raíz, se inserta
                                          // en el subárbol izquierdo.
            root.left = insert(root.left, newNode);
        } else { // Si el valor del nuevo node es mayor o igual que el valor del node raíz, se
                 // inserta en el subárbol derecho.
            root.right = insert(root.right, newNode);
        }
        return root;
    }

    // Método público que realiza un recorrido en orden ascendente del árbol e
    // imprime los valores de los nodes.
    public void inOrderTraversal() {
        inOrderTraversal(root); // Llamar al método privado inOrderTraversal para realizar el recorrido en orden
                                // ascendente.
    }

    // Método privado que realiza un recorrido en orden ascendente del subárbol y
    // imprime los valores de los nodes.
    private void inOrderTraversal(Node root) {
        if (root != null) { // Si el node raíz no es null, se recorre el subárbol en orden ascendente.
            inOrderTraversal(root.left); // Primero se recorre el subárbol izquierdo.
            System.out.print(root.value + " "); // Luego se imprime el valor del node raíz.
            inOrderTraversal(root.right); // Finalmente se recorre el subárbol derecho.
        }
    }

    // Método público que realiza un recorrido en preorden del árbol e imprime los
    // valores de los nodes.
    public void preOrderTraversal() {
        preOrderTraversal(root); // Llamar al método privado preOrderTraversal para realizar el recorrido en
                                 // preorden.
    }

    // Método privado que realiza un recorrido en preorden del subárbol y imprime
    // los valores de los nodes.
    private void preOrderTraversal(Node root) {
        if (root != null) { // Si el node raíz no es null, se recorre el subárbol en preorden.
            System.out.print(root.value + " "); // Primero se imprime el valor del node raíz.
            preOrderTraversal(root.left); // Luego se recorre el subárbol izquierdo.
            preOrderTraversal(root.right); // Finalmente se recorre el subárbol derecho.

        }
    }
}