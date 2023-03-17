public class Arbusto extends Planta {

    private String variety;
    private double width;

    public Arbusto() {
    }

    public Arbusto(int id, String name, double height, Boolean hasLeaves, String idealWeather, String variety,
            double width) {

        super(id, name, height, hasLeaves, idealWeather);
        this.variety = variety;
        this.width = width;
    }

    @Override
    public void name() {
        System.out.println("Hola soy un Arbusto");

    }

    public String getVariety() {
        return this.variety;
    }

    public void setVariety(String variety) {
        this.variety = variety;
    }

    public double getWidth() {
        return this.width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

}
