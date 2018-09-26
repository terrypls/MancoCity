import Varios
from Mancos import Shesho

diccionario = {"caca": "holi"}
diccionario["hola"] = Varios.hola()
diccionario["!F"] = Varios.F()
diccionario["manco"] = Varios.manco()
diccionario["!oniichan"] = Varios.Onichan()
diccionario["loli"] = Varios.loli()
diccionario["porno"] = Varios.porno()
diccionario["shesho"] = Shesho.shesho()

def Key(llave):
    x = diccionario[llave]
    return x


def agregar(llave, valor):
    diccionario[llave] = valor
