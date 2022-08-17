public class ConectivosLogicos //Se define la clase principal del script
{
    public static void main(String []args)
    {
        // En java para definir un arreglo se debe utilizar la siguiente sintaxis:
        // Tipodedato[] NombreDelArreglo = "new boolean[tamaño]" 
        //    donde tamaño tiene que ser un entero positivo
        boolean[] bool = new boolean[2]; 
        bool[0] = true;  
        bool[1] = false; 
        //Asignacion de indices desde el [0], [1] ; 
        // donde [0] corresponde a True y [1] a False
        
        //Negacion
        //Para este conectivo lógico se utiliza  “ ! ”
        //Ejemplo: ~p se representa !p
        System.out.println("Negación: p ~p");
        System.out.println("p\t~p");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            boolean P = !p;
            //ciclo for
            //se analizan los valores de p y q
            System.out.println(p + "\t" + P);
            //Se muestran los resultados por pantalla
        }
        //Conjuncion
        //Para este conectivo lógico se utiliza  “ && ”
        //Ejemplo: p & q se representa p && q 
        System.out.println("\nConjunción: p AND q");
        System.out.println("p\tq\tp AND q");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            for (boolean q: bool) {
                boolean P = p && q;
                //ciclo for
                //se analizan los valores de p y q
                System.out.println(p+"\t"+q+"\t"+P);
                //Se muestran los resultados por pantalla
            }
        }
        //Disyunción inclusiva
        //Para este conectivo lógico se utiliza  “ || ”
        //Ejemplo: p v q se representa p || q
        System.out.println("\nDisyunción inclusiva: p OR q");
        System.out.println("p\tq\tp OR q");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            for (boolean q: bool) {
                boolean P = p || q;
                //ciclo for
                //se analizan los valores de p y q
                System.out.println(p+"\t"+q+"\t"+P);
                //Se muestran los resultados por pantalla
            }
        }
        //Disyunción exclusiva
        //Para este conectivo lógico se utiliza  “ != ”.
        System.out.println("\nDisyunción exclusiva: p XOR q");
        System.out.println("p\tq\tp XOR q");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            for (boolean q: bool) {
                boolean P = p != q;
                //ciclo for
                //se analizan los valores de p y q
                System.out.println(p+"\t"+q+"\t"+P);
                //Se muestran los resultados por pantalla
            }
        }
        //Condicional
        //Para este conectivo lógico se utilizan  “ !, || ”
        System.out.println("\nCondicional: p -> q");
        System.out.println("p\tq\tp -> q");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            for (boolean q: bool) {
                boolean P = !p || q;
        //ciclo for
        //se analizan los valores de p y q
                System.out.println(p+"\t"+q+"\t"+P);
                //Se muestran los resultados por pantalla
            }
        }
        //Bicondicional
        //Para este conectivo lógico se utilizan  “ == ”
        System.out.println("\nBicondicional: p <-> q");
        System.out.println("p\tq\tp <-> q");
        //Se imprimen las proposiciones
        for (boolean p: bool) {
            for (boolean q: bool) {
                boolean P = p == q;
        //ciclo for
        //se analizan los valores de p y q
                System.out.println(p+"\t"+q+"\t"+P);
        //Se muestran los resultados por pantalla
            }
        }
    }
}


