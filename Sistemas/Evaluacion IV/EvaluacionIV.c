#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>

int memoria;

pthread_mutex_t numeros = PTHREAD_MUTEX_INITIALIZER;

void *crearrandoms()
{
    int i;

    srand(time(NULL));

    for (i = 0; i < 10; i++)
    {
        pthread_mutex_lock(&numeros);

        memoria = 1 + rand() % (10 - 1);
        printf("Padre escribiendo: %d\n", memoria);

        pthread_mutex_unlock(&numeros);

        usleep(200);
    }

    printf("\n \n");
    return 0;
}

void *leerrandoms()
{
    int i;
    int arreglo[10];
    int suma;

    float promedio;

    usleep(100);

    for (i = 0; i < 10; i++)
    {
        pthread_mutex_lock(&numeros);

        printf("Hijo Leyendo: %d\n", memoria);

        arreglo[i] = memoria;
        suma = suma + arreglo[i];

        pthread_mutex_unlock(&numeros);
        usleep(200);
    }

    promedio = suma / 10; /* El promedio funciona, pero no se muestra en el txt, no entendí por qué. */

    printf("El promedio es: %f\n", promedio);

    FILE *archivo;

    archivo = fopen("resultados.txt", "w");

    fprintf(archivo, "Los numeros son: %d, %d, %d, %d, %d, %d, %d, %d, %d, %d y el promedio es: %d\n", arreglo[0], arreglo[1], arreglo[2], arreglo[3], arreglo[4], arreglo[5], arreglo[6], arreglo[7], arreglo[8], arreglo[9], promedio);
}

int main()
{
    pthread_t hilo0, hilo1;

    pthread_create(&hilo0, NULL, (void *)&crearrandoms, NULL);
    pthread_create(&hilo1, NULL, (void *)&leerrandoms, NULL);

    pthread_join(hilo0, NULL);
    pthread_join(hilo1, NULL);

    return 0;
}