def openfile():
    filefruta = open('file1.txt', 'a')
    ingresa=input("- Ingrese informacion para el archivo txt: ")
    filefruta.write(ingresa)
    return

openfile()