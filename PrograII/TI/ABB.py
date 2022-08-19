# "Arboles" son estructuras donde los datos se organizan jerarquícamente
# y estan vinculados entre sí(se diferencian de las listas enlazadas 
# ya que estas estan enlazadas de forma lineal).


class binarytree:
    
    """La clase binarytree tiene su raiz, hijo izquierdo e hijo derecho.
    La raiz al llamar a la clase se le asigna un valor, por lo contrario
    el arbol binario no tendra hijos"""

    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None 
        self.left = None
        self.right = None

    """para insertar un valor la función recorre el arbol.
    lo primero que hace es verificar si en el nodo actual hay un
    valor, si no hay le asigna el valor a ese nodo, por lo contrario
    si el valor es menor que el valor del nodo verifica que la
    izquierda del nodo padre(en ese momento) este "vacio" si lo esta,
    a travez de la recursividad asigna el valor a el hijo izquierdo
    de ese nodo padre, si no llama a la función insert pero ahora el
    nodo padre es el hijo izquierdo de la operación anterior. cuando
    el valor es mayor ocurre lo mismo pero con el hijo derecho"""

    def Insert(self, val):
        if self.val:
            if self.val == val:
                print(f"No se puede repetir un elemento: {val}")
            if val < self.val:
                if self.left is None:
                    self.left = binarytree(val)
                else:
                    self.left.Insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = binarytree(val)
                else:
                    self.right.Insert(val)
        else:
            self.val = val

    """Para imprimir un arbol binario de búsqueda se recorre de izquierda
    a derecha y de abajo hacia arriba
    Si hay un nodo a la izquierda del nodo padre, vuelve a llamar a la
    función y ese nodo a la izquierda pasa a ser el nuevo nodo padre,
    y asi sucecivamente hasta llegar a la derecha."""

    def PrintValues(self):
        if self.left:
            self.left.PrintValues()

        print(self.val)

        if self.right:
            self.right.PrintValues()

# tree = binarytree("F")
tree = binarytree(8)
if tree.val == None:
    print(tree.val)
else:
    tree.left = binarytree(5)
    tree.right = binarytree(10)
    # tree.left = binarytree("C")
    # tree.right = binarytree("I")
    # tree.Insert("A")
    # tree.Insert("K")
    # tree.Insert("H")
    # tree.Insert("D")
    tree.Insert(20)
    tree.Insert(7)
    tree.Insert(-3)
    tree.Insert(100)
    tree.Insert(7)
    tree.Insert(13)
    print("Los valores del ABB son:")
    tree.PrintValues()