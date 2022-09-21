public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche();
        coche.addPuerta();
        coche.addPuerta();
        coche.addPuerta();
        System.out.println(coche.nPuertas);
    }

}

class Coche {
    public int nPuertas = 0;

    public void addPuerta(){
        this.nPuertas++;
    }
}
