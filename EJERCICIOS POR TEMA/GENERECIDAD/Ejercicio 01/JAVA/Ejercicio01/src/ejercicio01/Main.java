package ejercicio01;

public class Main {
    public static void main(String[] args) {
        Caja<String> cajaDeTexto = new Caja<>();
        cajaDeTexto.guardar("Hola, mundo");
        System.out.println("Contenido de la caja: " + cajaDeTexto.obtener());

        Caja<Integer> cajaDeEnteros = new Caja<>();
        cajaDeEnteros.guardar(42);
        System.out.println("Contenido de la caja: " + cajaDeEnteros.obtener());
    }
}
