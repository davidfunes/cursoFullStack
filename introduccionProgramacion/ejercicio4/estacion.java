public class Program
{
	public static void main(String[] args) {
	
		String estacion = "invierno";
	
		switch (estacion){
		    case "primavera":
		    	System.out.println("Es " + estacion + "!");
		    	break;
		    case "verano":
		      	System.out.println("Es " + estacion + "!");
		    	break;
		    case "otoño" :
		    	System.out.println("Es " + estacion + "!");
		    	break;
		    case "invierno":
		    	System.out.println("Es " + estacion + "!");
		    	break;
		    default:
		    	System.out.println(estacion + " no es ninguna estación!");
		}
	}
}
