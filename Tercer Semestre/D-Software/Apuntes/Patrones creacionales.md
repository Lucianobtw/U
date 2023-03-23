Los patrones de creación proporcionan diversos mecanismos de creación de ***objetos***, que aumentan la **flexibilidad y la reutilización del código existente de una manera adecuada a la situación**. Esto le da al programa más flexibilidad para decidir qué objetos deben crearse para un caso de uso dado.

Estos son los **patrones creacionales**:

### Abstract Factory

En este patrón, una interfaz crea conjuntos o familias de objetos relacionados sin especificar el nombre de la clase.

### Builder Patterns

Permite producir diferentes tipos y representaciones de un objeto utilizando el mismo código de construcción. Se utiliza para la creación etapa por etapa de un objeto complejo combinando objetos simples. La creación final de objetos depende de las etapas del proceso creativo, pero es independiente de otros objetos.

### Factory Method

Proporciona una interfaz para crear objetos en una superclase, pero permite que las subclases alteren el tipo de objetos que se crearán. Proporciona instanciación de objetos implícita a través de interfaces comunes

### Prototype

Permite copiar objetos existentes sin hacer que su código dependa de sus clases. Se utiliza para restringir las operaciones de memoria / base de datos manteniendo la modificación al mínimo utilizando copias de objetos.

### Singleton

Este patrón de diseño restringe la creación de instancias de una clase a un único objeto.