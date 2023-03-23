public abstract class Planta {

    private int id;
    private String name;
    private double height;
    private Boolean hasLeaves;
    private String idealWeather;

    public Planta() {
    }

    public Planta(int id, String name, double height, Boolean hasLeaves, String idealWeather) {
        this.id = id;
        this.name = name;
        this.height = height;
        this.hasLeaves = hasLeaves;
        this.idealWeather = idealWeather;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getHeight() {
        return this.height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public Boolean isHasLeaves() {
        return this.hasLeaves;
    }

    public Boolean getHasLeaves() {
        return this.hasLeaves;
    }

    public void setHasLeaves(Boolean hasLeaves) {
        this.hasLeaves = hasLeaves;
    }

    public String getIdealWeather() {
        return this.idealWeather;
    }

    public void setIdealWeather(String idealWeather) {
        this.idealWeather = idealWeather;
    }

    public abstract void name();

    @Override
    public String toString() {
        return "{" +
                " id='" + getId() + "'" +
                ", name='" + getName() + "'" +
                ", height='" + getHeight() + "'" +
                ", hasLeaves='" + isHasLeaves() + "'" +
                ", idealWeather='" + getIdealWeather() + "'" +
                "}";
    }
}
