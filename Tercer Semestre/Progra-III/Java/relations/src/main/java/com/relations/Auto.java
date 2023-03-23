package com.relations;

import java.util.List;

public class Auto {

    private Long id;
    private String marca;
    private String modelo;

    // 1 - 1 (Un dueño)
    // private Propietario owner;

    // 1 - N (Muchos dueños)
    private List<Propietario> ownerList;

    public Auto() {
    }

    /*
     * Un dueño
     * 
     * public Auto(Long id, String marca, String modelo, Propietario owner) {
     * this.id = id;
     * this.marca = marca;
     * this.modelo = modelo;
     * this.owner = owner;
     * }
     */

    // Varios dueños

    public Auto(Long id, String marca, String modelo, List<Propietario> ownerList) {
        this.id = id;
        this.marca = marca;
        this.modelo = modelo;
        this.ownerList = ownerList;
    }

    // Getters y Setters

    public Long getId() {
        return this.id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return this.modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    /*
     * Un dueño
     * 
     * public Propietario getOwner() {
     * return this.owner;
     * }
     * 
     * public void setOwner(Propietario owner) {
     * this.owner = owner;
     * }
     * 
     */

    // Muchos dueños

    public List<Propietario> getOwnerList() {
        return this.ownerList;
    }

    public void setOwnerList(List<Propietario> ownerList) {
        this.ownerList = ownerList;
    }

    @Override
    public String toString() {
        return "{" +
                " id='" + getId() + "'" +
                ", marca='" + getMarca() + "'" +
                ", modelo='" + getModelo() + "'" +
                ", ownerList='" + getOwnerList() + "'" +
                "}";
    }

}
