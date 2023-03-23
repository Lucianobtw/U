package com.pokemon;

public abstract class Pokemon {

    protected int pokedexNum;
    protected String pokemonName;
    protected int pokemonWeight;
    protected String pokemonSex;
    protected String season;
    protected String pokemonType;

    protected abstract void tackleAttack();

    protected abstract void scratchAttack();

    protected abstract void nibbleAttack();

}

// Una Clase abstracta es una clase que no se puede instanciar,
// es decir, no se puede crear un objeto de esa clase.

// Su función es ser una clase base para otras clases que hereden de ella.
