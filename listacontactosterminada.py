# -*- coding: utf-8 -*-

class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.next = None
        self.prev = None

    def getelemento(self):
        return self.apellido

class list:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def insertar(self,nombre, apellido, telefono, mail):  #insertar por apellido
        contacto = Node(nombre, apellido, telefono, mail)
        if self.empty():
            self.head = contacto

        elif self.head.apellido > contacto.apellido:
            contacto.next = self.head
            self.head.prev = contacto
            self.head = contacto
        elif self.head.apellido == contacto.apellido and self.head.nombre > contacto.nombre:
            contacto.next = self.head
            self.head.prev = contacto
            self.head = contacto
        else:
            aux = self.head
            while True:
                if aux.apellido > contacto.apellido :
                    contacto.next = aux
                    contacto.prev = aux.prev
                    aux.prev.next = contacto
                    aux.prev = contacto
                    break
                elif aux.apellido == contacto.apellido and aux.nombre > contacto.nombre:
                    contacto.next = aux
                    contacto.prev = aux.prev
                    aux.prev.next = contacto
                    aux.prev = contacto
                    break
                elif aux.next == None:
                    aux.next = contacto
                    contacto.prev = aux
                    break
                aux = aux.next


    def buscar(self, apellido, nombre):     #busca por un apellido entregado
        aux = self.head
        while True:
            if aux.apellido == apellido and aux.nombre == nombre:
                print(aux.nombre, aux.apellido, aux.telefono, aux.mail)
                break
            aux = aux.next

    def eliminar(self, apellido, nombre): #se entrega el apellido y lo busca para eliminarlo
        if self.head.apellido == apellido and self.head.nombre == nombre:
            self.head.next.prev == None
            self.head = self.head.next

        else:
            aux1=self.head
            while True:
                if aux1.apellido == apellido and aux1.nombre == nombre:
                    aux1.prev = aux1.next
                    aux1.next = aux1.prev
                    gc.collect()
                    break
                aux1=aux1.next

    def imprimir(self):
        aux = self.head
        while aux is not None:
            print(aux.apellido+", "+aux.nombre+", "+aux.telefono+", "+aux.mail)
            aux = aux.next

def main():        
    while True:
        print("Seleccione una opcion: ")
        print("1.Agregar contacto")
        print("2.Buscar contacto")
        print("3.Eliminar contacto")
        print("4.Ver lista completa")
        aux = input()
        ldc = list()
        if aux == 1:
            print("Ingrese nombre: ")
            nombre = input()
            print("apellido: ")
            apellido = input()
            print("telefono: ")
            telefono = input()
            print("mail: ")
            mail = input()
            ldc.insertar(nombre, apellido, telefono, mail)
            print("Contacto guardado.")
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 2:
            print("Ingrese el apellido y el nombre del contacto que esta buscando: ")
            apellido = input()
            nombre = input()
            ldc.buscar(apellido, nombre)
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 3:
            print("Ingrese el nombre y apellido del contacto que desea eliminar: ")
            nombre = input()
            apellido = input()
            ldc.eliminar(apellido, nombre)
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 4:
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
