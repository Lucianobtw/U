package com.games;

import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) {

        List<Videojuego> gamesArray = new ArrayList<>();

        createGames(gamesArray);
        showGameData(gamesArray);
        getN64games(gamesArray);
    }

    public static void createGames(List<Videojuego> gamesArray) {

        Videojuego game_1 = new Videojuego(1, "Call of duty 1", "PS2", 10000, "FPS");
        Videojuego game_2 = new Videojuego(2, "Call of duty 2", "PS2", 10000, "FPS");
        Videojuego game_3 = new Videojuego(3, "Call of duty 3", "PS3", 100000, "FPS");
        Videojuego game_4 = new Videojuego(4, "Super Smash Bros", "Nintendo 64", 100, "Adventure");
        Videojuego game_5 = new Videojuego(5, "Super Mario 64", "Nintendo 64", 100, "Adventure");

        gamesArray.add(game_1);
        gamesArray.add(game_2);
        gamesArray.add(game_3);
        gamesArray.add(game_4);
        gamesArray.add(game_5);

    }

    public static void showGameData(List<Videojuego> gamesArray) {

        for (Videojuego game : gamesArray) {
            game.getAll();
        }

    }

    public static void getN64games(List<Videojuego> gamesArray) {

        System.out.println("|---------| N64 Games |------------| ");

        for (Videojuego game : gamesArray) {
            if (game.getConsole().equals("Nintendo 64")) {
                game.getAll();
            }
        }

    }
}
