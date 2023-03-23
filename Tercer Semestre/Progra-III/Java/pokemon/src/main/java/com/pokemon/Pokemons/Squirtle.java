package com.pokemon.Pokemons;

import com.pokemon.Pokemon;
import com.pokemon.Types.IWater;

public class Squirtle extends Pokemon implements IWater {

    public Squirtle() {
    }

    // Default attacks

    @Override
    public void tackleAttack() {
        System.out.println("Squirtle used Tackle!");
    }

    @Override
    public void scratchAttack() {
        System.out.println("Squirtle used Scratch!");
    }

    @Override
    public void nibbleAttack() {
        System.out.println("Squirtle used Nibble!");
    }

    // Water type attacks

    @Override
    public void waterGun() {
        System.out.println("Squirtle used Water Gun!");
    }

    @Override
    public void hydroPump() {
        System.out.println("Squirtle used Hydro Pump!");
    }

    @Override
    public void surf() {
        System.out.println("Squirtle used Surf!");
    }

}
