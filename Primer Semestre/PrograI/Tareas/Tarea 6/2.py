"""Luego abre el archivo anteriormente generado, extrae la información almacenando el
contenido en una lista y muestra por pantalla. (2 puntos)"""

filefruta = open('file1.txt', 'r')
print(filefruta.readlines())
filefruta.close()