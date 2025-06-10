import java.io.*;
import java.util.*;

public class ProductoManager {
    private static final String ARCHIVO = "productos.txt";

    public static List<Producto> cargarProductos() {
        List<Producto> lista = new ArrayList<>();
        File archivo = new File(ARCHIVO);

        if (!archivo.exists()) return lista;

        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                String[] partes = linea.split(";");
                if (partes.length == 3) {
                    String nombre = partes[0];
                    double precio = Double.parseDouble(partes[1]);
                    int cantidad = Integer.parseInt(partes[2]);
                    lista.add(new Producto(nombre, precio, cantidad));
                }
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }

        return lista;
    }

    public static void guardarProductos(List<Producto> productos) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(ARCHIVO))) {
            for (Producto p : productos) {
                String linea = p.getNombre() + ";" + p.getPrecio() + ";" + p.getCantidad();
                bw.write(linea);
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Error al guardar el archivo: " + e.getMessage());
        }
    }
}
