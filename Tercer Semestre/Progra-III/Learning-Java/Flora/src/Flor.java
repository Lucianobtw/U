
public class Flor extends Planta {

    private String variety;

    public Flor() {
    }

    public Flor(int id, String name, double height, Boolean hasLeaves, String idealWeather, String variety) {
        super(id, name, height, hasLeaves, idealWeather);
        this.variety = variety;
    }

    public String getVariety() {
        return this.variety;
    }

    public void setVariety(String variety) {
        this.variety = variety;
    }

    @Override
    public void name() {
        System.out.println("Hola soy una Flor");
    }

}
