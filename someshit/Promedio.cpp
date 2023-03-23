
#include <iostream>
#include <cstdio>

int main() {
  
  int cantNotas;
  float nota;
  float porcentaje;
  float promedio = 0;

  std::cout << "Ingresa el número de notas (cantidad): " << std::endl;
  std::cin >> cantNotas;

  float notas[cantNotas]; 
  float porcentajes[cantNotas];

  for (int i = 0; i < cantNotas; i++) {

    std::cout << "Ingresa la nota número " << i + 1 << ": " << std::endl;
    std::cin >> nota;

    std::cout << "Ingresa la ponderación: " << std::endl;
    std::cin >> porcentaje;

    notas[i] = nota;
    porcentajes[i] = porcentaje;
  }

  for (int i = 0; i < cantNotas; i++) {  

    promedio += notas[i] * porcentajes[i];
  }

  printf("Tu promedio es: %f \n", promedio);

  return 0;
}


   
