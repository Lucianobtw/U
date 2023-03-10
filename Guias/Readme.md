# Curso git Mastermind

## Basics

### Inicializar repositorio en local:

``` git init ```

### Verificar estado del repositorio:

``` git status ```

### Agregar archivos al repositorio:

``` git add <nombre_archivo> || git add . (agrega todos los archivos) ```

### Confirmar cambios y crear commit:

``` git commit -m "mensaje" ```

### Ver historial de commits:

``` git log --oneline ```

### Subir cambios 
    
``` git push ```

## Branches

### Crear rama y cambiar a ella:

``` git checkout -b <nombre_rama> ```

### Cambiar a rama existente:

``` git checkout <nombre_rama> ```

### Ver ramas existentes:

``` git branch ```

## Extras

### Volver a un commit anterior:

``` git reset --hard <id_commit> (Ver con git log --oneline) ```

### Subir cambios locales a repositorio remoto:

``` git remote add origin <url_repositorio> ```
``` git push -u origin master ```

