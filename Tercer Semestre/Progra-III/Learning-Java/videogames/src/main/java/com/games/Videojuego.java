package com.games;

public class Videojuego {

    private int code;
    private String title;
    private String console;
    private int numOfPlayers;
    private String category;

    public Videojuego() {
    }

    public Videojuego(int code, String title, String console, int numOfPlayers, String category) {
        this.code = code;
        this.title = title;
        this.console = console;
        this.numOfPlayers = numOfPlayers;
        this.category = category;
    }

    public int getCode() {
        return this.code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getConsole() {
        return this.console;
    }

    public void setConsole(String console) {
        this.console = console;
    }

    public int getNumOfPlayers() {
        return this.numOfPlayers;
    }

    public void setNumOfPlayers(int numOfPlayers) {
        this.numOfPlayers = numOfPlayers;
    }

    public String getCategory() {
        return this.category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    @Override
    public String toString() {
        return "{" +
                " code='" + getCode() + "'" +
                ", title='" + getTitle() + "'" +
                ", console='" + getConsole() + "'" +
                ", numOfPlayers='" + getNumOfPlayers() + "'" +
                ", category='" + getCategory() + "'" +
                "}";
    }

    public void getAll() {
        System.out.println("|----------------------------------|");
        System.out.println("|- Code: " + getCode());
        System.out.println("|- Title: " + getTitle());
        System.out.println("|- Platform: " + getConsole());
        System.out.println("|- Players: " + getNumOfPlayers());
        System.out.println("|- Category: " + getCategory() + "\n");
    }

}
