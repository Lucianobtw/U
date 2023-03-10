package com.pokemon.Pokemons;

import com.pokemon.Pokemon;
import com.pokemon.Types.IFire;

public class Charmander extends Pokemon implements IFire {

    public Charmander() {
    }

    // Default attacks

    @Override
    public void tackleAttack() {
        System.out.println("Charmander used Tackle!");
    }

    @Override
    public void scratchAttack() {
        System.out.println("Charmander used Scratch!");
    }

    @Override
    public void nibbleAttack() {
        System.out.println("Charmander used Nibble!");
    }

    // Fire type attacks

    @Override
    public void firePunch() {
        System.out.println("Charmander used Ember!");
    }

    @Override
    public void fireBlast() {
        System.out.println("Charmander used Fire Blast!");
    }

    @Override
    public void flameThrower() {
        System.out.println("Charmander used Flame Thrower!");
    }

}
