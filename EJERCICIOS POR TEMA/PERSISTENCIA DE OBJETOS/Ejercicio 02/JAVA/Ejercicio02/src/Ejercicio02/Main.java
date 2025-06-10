import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Producto> productos = ProductoManager.cargarProductos();

        while (true) {
            System.out.println("\n1. Agregar producto");
            System.out.println("2. Mostrar productos");
            System.out.println("3. Salir");
            System.out.print("Opción: ");
            String opcion = sc.nextLine();

            switch (opcion) {
                case "1":
                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Precio: ");
                    double precio = Double.parseDouble(sc.nextLine());
                    System.out.print("Cantidad: ");
                    int cantidad = Integer.parseInt(sc.nextLine());
                    Producto nuevo = new Producto(nombre, precio, cantidad);
                    productos.add(nuevo);
                    ProductoManager.guardarProductos(productos);
                    System.out.println("Producto guardado.");
                    break;
                case "2":
                    if (productos.isEmpty()) {
                        System.out.println("No hay productos registrados.");
                    } else {
                        for (Producto p : productos) {
                            System.out.println(p);
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
