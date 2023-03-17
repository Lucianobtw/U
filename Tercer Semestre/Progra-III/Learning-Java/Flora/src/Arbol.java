public class Arbol extends Planta {

    private String variety;

    public Arbol() {
    }

    public Arbol(int id, String name, double height, Boolean hasLeaves, String idealWeather, String variety) {
        super(id, name, height, hasLeaves, idealWeather);
        this.variety = variety;
    }

    @Override
    public void name() {
        System.out.println("Hola, soy un arbol");
    }

    public String getVariety() {
        return this.variety;
    }

    public void setVariety(String variety) {
        this.variety = variety;
    }

}
