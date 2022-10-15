#include <string.h>
#include <unistd.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

void *create_shared_memory(size_t size)
{
    // La memoria del buffer será legible y escribible
    int protection = PROT_READ | PROT_WRITE;

    // El buffer será compartido (es decir, otros procesos podrán acceder a él), pero
    //  anónimo (es decir, los procesos de terceros no podrán obtener una dirección para él),
    //  por lo que solo este proceso y sus hijos podrán usarlo:

    int visibility = MAP_SHARED | MAP_ANONYMOUS;

    // Los parámetros restantes para `mmap ()` no son importantes para este caso de uso,
    // pero la página de manual para `mmap` explica su propósito.
    return mmap(NULL, size, protection, visibility, -1, 0);
}

int main()
{
    char parent_message[] = "hello";  // El proceso padre escribirá este mensaje
    char child_message[] = "goodbye"; // El proceso hijo escribirá este mensaje

    void *shmem = create_shared_memory(128);

    memcpy(shmem, parent_message, sizeof(parent_message));

    int pid = fork();

    if (pid == 0)
    {
        printf("Child read: %s\n", shmem);
        memcpy(shmem, child_message, sizeof(child_message));
        printf("Child wrote: %s\n", shmem);
    }
    else
    {
        printf("Parent read: %s\n", shmem);
        sleep(1);
        printf("After 1s, parent read: %s\n", shmem);
    }
}
