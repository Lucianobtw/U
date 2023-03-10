package com.pokemon;

import com.pokemon.Pokemons.Bullbasaur;
import com.pokemon.Pokemons.Charmander;
import com.pokemon.Pokemons.Pikachu;
import com.pokemon.Pokemons.Squirtle;

public class App {
    public static void main(String[] args) {

        Bullbasaur bullbasaur = new Bullbasaur();
        Charmander charmander = new Charmander();

        Pikachu pikachu = new Pikachu();
        Squirtle squirtle = new Squirtle();

        bullbasaur.tackleAttack();
        charmander.scratchAttack();
        pikachu.nibbleAttack();
        squirtle.tackleAttack();

        bullbasaur.razorLeaf();
        charmander.flameThrower();
        pikachu.thunderShock();
        squirtle.waterGun();
    }
}
