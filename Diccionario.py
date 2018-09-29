import Varios
diccionario = {"ayuda": Varios.ayuda()}
def inicio():
    file = open('Palabras.txt', 'r')
    for line in file:
        aux = line.split(" ", 1)
        diccionario[aux[0]] = aux[1]

    file.close()
diccionario["porno"] = Varios.porno()



def addFile(llave, valor):
    file = open('Palabras.txt', 'a')
    file.write(llave + ' ' + valor)
    file.close()
    inicio()



def Key(llave):
    x = diccionario[llave]
    return x


def agregar(llave, valor):
    diccionario[llave] = valor
