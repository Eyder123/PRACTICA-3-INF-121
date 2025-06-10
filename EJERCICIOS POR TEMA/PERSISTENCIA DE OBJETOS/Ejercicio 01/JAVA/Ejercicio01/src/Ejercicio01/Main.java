import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Estudiante> estudiantes = EstudianteManager.cargarEstudiantes();

        while (true) {
            System.out.println("\n1. Agregar estudiante");
            System.out.println("2. Mostrar estudiantes");
            System.out.println("3. Salir");
            System.out.print("Opción: ");
            String opcion = sc.nextLine();

            switch (opcion) {
                case "1":
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Edad: ");
                    int edad = Integer.parseInt(sc.nextLine());
                    System.out.print("Carrera: ");
                    String carrera = sc.nextLine();
                    Estudiante nuevo = new Estudiante(nombre, edad, carrera);
                    estudiantes.add(nuevo);
                    EstudianteManager.guardarEstudiantes(estudiantes);
                    System.out.println("Estudiante guardado.");
                    break;
                case "2":
                    if (estudiantes.isEmpty()) {
                        System.out.println("No hay estudiantes registrados.");
                    } else {
                        for (Estudiante e : estudiantes) {
                            System.out.println(e);
                        }
                    }
                    break;
                case "3":
                    return;
                default:
                    System.out.println("Opción inválida.");
            }
        }
    }
}
