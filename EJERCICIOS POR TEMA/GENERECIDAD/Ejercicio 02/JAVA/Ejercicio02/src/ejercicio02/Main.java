package ejercicio02;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String[] palabras = {"uno", "dos", "tres"};
        System.out.println("Antes: " + Arrays.toString(palabras));
        Utilidades.intercambiar(palabras, 0, 2);
        System.out.println("Después: " + Arrays.toString(palabras));

        Integer[] numeros = {1, 2, 3};
        System.out.println("Antes: " + Arrays.toString(numeros));
        Utilidades.intercambiar(numeros, 1, 2);
        System.out.println("Después: " + Arrays.toString(numeros));
    }
}
