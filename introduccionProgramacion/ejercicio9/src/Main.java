public class Main
{
	public static void main(String[] args) {
		Cliente cliente = new Cliente();
		Trabajador trabajador = new Trabajador();
		
		cliente.setEdad(42);
		cliente.setNombre("David");
		cliente.setTelefono(999999999);
		cliente.setCredito(299999.99);
		System.out.println("El nombre del cliente es: " + cliente.getNombre());
		System.out.println("La edad es: " + cliente.getEdad());
		System.out.println("El teléfono es: " + cliente.getTelefono());
		System.out.println("El crédito disponible es: " + cliente.getCredito() + "€");
		
		System.out.println();
		
		trabajador.setEdad(34);
		trabajador.setNombre("Júlia");
		trabajador.setTelefono(999999999);
		trabajador.setSalario(3000.57);
		System.out.println("El nombre del trabajador es: " + trabajador.getNombre());
		System.out.println("La edad es: " + trabajador.getEdad());
		System.out.println("El teléfono es: " + trabajador.getTelefono());
		System.out.println("El salario es: " + trabajador.getSalario() + "€ mensuales.");
		
	}
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;
    
    public void setEdad(int edad){
        this.edad = edad;
    }
    
    public int getEdad(){
        return this.edad;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    
    public int getTelefono(){
        return this.telefono;
    }
   
}

class Cliente extends Persona{
    private double credito;
    
    public void setCredito(double credito){
        this.credito = credito;
    }
    
    public double getCredito(){
        return this.credito;
    }
}

class Trabajador extends Persona{
    private double salario;
    
    public void setSalario(double salario){
        this.salario = salario;
    }
    
    public double getSalario(){
        return this.salario;
    }
}
