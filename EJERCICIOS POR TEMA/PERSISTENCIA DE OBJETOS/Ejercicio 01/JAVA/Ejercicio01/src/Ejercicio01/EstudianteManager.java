import java.io.*;
import java.util.*;

public class EstudianteManager {
    private static final String ARCHIVO = "estudiantes.txt";

    public static List<Estudiante> cargarEstudiantes() {
        List<Estudiante> lista = new ArrayList<>();
        File archivo = new File(ARCHIVO);

        if (!archivo.exists()) return lista;

        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(";");
                if (partes.length == 3) {
                    String nombre = partes[0];
                    int edad = Integer.parseInt(partes[1]);
                    String carrera = partes[2];
                    lista.add(new Estudiante(nombre, edad, carrera));
                }
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }

        return lista;
    }

    public static void guardarEstudiantes(List<Estudiante> estudiantes) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ARCHIVO))) {
            for (Estudiante e : estudiantes) {
                String linea = e.getNombre() + ";" + e.getEdad() + ";" + e.getCarrera();
                bw.write(linea);
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error al guardar el archivo: " + e.getMessage());
        }
    }
}
