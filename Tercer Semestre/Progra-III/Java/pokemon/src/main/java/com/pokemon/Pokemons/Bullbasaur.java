package com.pokemon.Pokemons;

import com.pokemon.Pokemon;
import com.pokemon.Types.IGrass;

public class Bullbasaur extends Pokemon implements IGrass {

    public Bullbasaur() {
    }

    // Default attacks

    @Override
    public void tackleAttack() {
        System.out.println("Bullbasaur used Tackle!");
    }

    @Override
    public void scratchAttack() {
        System.out.println("Bullbasaur used Scratch!");
    }

    @Override
    public void nibbleAttack() {
        System.out.println("Bullbasaur used Nibble!");
    }

    // Grass type attacks

    @Override
    public void razorLeaf() {
        System.out.println("Bullbasaur used Razor Leaf!");
    }

    @Override
    public void vineWhip() {
        System.out.println("Bullbasaur used Vine Whip!");
    }

    @Override
    public void solarBeam() {
        System.out.println("Bullbasaur used Solar Beam!");
    }

}
