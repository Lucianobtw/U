package com.pokemon.Pokemons;

import com.pokemon.Pokemon;
import com.pokemon.Types.IElectric;

public class Pikachu extends Pokemon implements IElectric {

    public Pikachu() {
    }

    // Default attacks

    @Override
    public void tackleAttack() {
        System.out.println("Pikachu used Tackle!");
    }

    @Override
    public void scratchAttack() {
        System.out.println("Pikachu used Scratch!");
    }

    @Override
    public void nibbleAttack() {
        System.out.println("Pikachu used Nibble!");
    }

    // Electric type attacks

    @Override
    public void thunderbolt() {
        System.out.println("Pikachu used Thunder Shock!");
    }

    @Override
    public void thunder() {
        System.out.println("Pikachu used Thunder!");
    }

    @Override
    public void thunderShock() {
        System.out.println("Pikachu used Thunder Shock!");
    }
}
