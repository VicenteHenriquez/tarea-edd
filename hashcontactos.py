# -*- coding: utf-8 -*-

def str2num(key):
  return sum([ord(c) for c in key])

def hashstr(key,size):
  return str2num(key)%size


class hash:
    def __init__(self,size):
        self.list = [None]*size
        self.size= size

    def insertar(self,key,nombre,telefono,mail):  #key = apellido
        pos = hashstr(key,self.size)
        if self.list[pos] is not None:
            print("collision "+key+"<br>")
            ok = False
            for t in self.list[pos]:
                if t[0] is key:
                    t[1] = nombre+", "+key+", "+telefono+", "+mail
                    ok = True
            if not ok:
                self.list[pos].append([key,nombre,telefono,mail])
        else:
            self.list[pos] =[]
            self.list[pos].append([key,nombre+", "+key+", "+telefono+", "+mail])

    def Buscar(self,key):
        for e in self.list[hashstr(key,self.size)]:
            if e[0] is key:
                print e[1]
    def imprimir(self):
        for e in self.list[hashstr(key,self.size)]:
           print e[1]

def main():
    while True:
        print("Seleccione una opcion: ")
        print("1.Agregar contacto")
        print("2.Buscar contacto")
        print("3.Ver lista completa")
        aux = input()
        ldc = hash(100)
        if aux == 1:
            print("Ingrese nombre: ")
            nombre = input()
            print("apellido: ")
            apellido = input()
            print("telefono: ")
            telefono = input()
            print("mail: ")
            mail = input()
            ldc.insertar(apellido, nombre, telefono, mail)
            print("Contacto guardado.")
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 2:
            print("Ingrese el apellido del contacto que esta buscando: ")
            apellido = input()
            ldc.Buscar(apellido)
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 3:
            print("Imprimiendo lista de contactos: ")
            ldc.imprimir()
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        else:
            print("Buen dia")
            break
