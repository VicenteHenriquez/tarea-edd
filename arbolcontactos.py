# -*- coding: utf-8 -*-

class Node:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.left = None
        self.right = None
        self.parent = None

class arboldecontactos:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def _insertar(self, nombre, apellido,telefono,mail, node):
        if apellido < node.apellido:
            if node.left == None:
                node.left = Node(nombre, apellido,telefono,mail)
                node.left.parent = node
            else:
                self._insertar(nombre, apellido,telefono,mail, node.left)
        elif apellido > node.apellido:
            if node.right == None:
                node.right = Node(nombre, apellido,telefono,mail)
                node.right.parent = node
            else:
                self._insertar(nombre,apellido,telefono,mail, node.right)
        else:
            if nombre < node.nombre:
                if node.left == None:
                    node.left = Node(nombre, apellido,telefono,mail)
                    node.left.parent = node
                else:
                    self._insertar(nombre, apellido,telefono,mail, node.left)
            else:
                if node.right == None:
                    node.right = Node(nombre, apellido,telefono,mail)
                    node.right.parent = node
                else:
                    self._insertar(nombre,apellido,telefono,mail, node.right)

    def insertar(self,nombre, apellido,telefono,mail):
        if self.empty():
            self.root = Node(nombre, apellido,telefono,mail)
        else:
            self._insertar(nombre, apellido,telefono,mail, self.root)

    def _buscar(self, nombre, apellido, node):
        if node == None:
            return None
        elif apellido == node.apellido and nombre == node.nombre:
            return node
        elif apellido < node.apellido and node.left != None:
            return self._buscar(nombre, apellido, node.left)
        elif apellido > node.apellido and node.right != None:
            return self._buscar(nombre, apellido, node.right)

    def buscar(self, apellido, nombre):
        if self.empty():
            return None
        else:
            return self._find(apellido, nombre, self.root)

    def eliminar_contacto(self, node):
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        def number_children(n):
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = node.parent
        node_children = number_children(node)

        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None
        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            child.parent = node_parent
        if node_children == 2:
            successor = min_value_node(node.right)
            node.apellido = successor.apellido
            node.nombre = successor.nombre
            node.telefono = successor.telefono
            node.mail = successor.mail
            self.eliminar_contacto(successor)

    def eliminar(self, nombre, apellido):
        if self.empty():
            return None
        return self.eliminar_contacto(self.buscar(apellido, nombre))


    def imprimir(self, node):
        if node==None:
            pass
        else:
            self.imprimir(node.left)
            print(node.apellido +", "+ node.nombre +", "+ node.telefono +", "+ node.mail)
            self.imprimir(node.right)

def main():
    while True:
        print("Seleccione una opcion: ")
        print("1.Agregar contacto")
        print("2.Buscar contacto")
        print("3.Eliminar contacto")
        print("4.Ver lista completa")
        aux = input()
        ldc = arboldecontactos()
        if aux == 1:
            print("Ingrese nombre: ")
            nombre = input()
            print("apellido: ")
            apellido = input()
            print("telefono: ")
            telefono = input()
            print("mail: ")
            mail = input()
            contacto = Node(nombre, apellido, telefono, mail)
            ldc.insertar(contacto)
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
            ldc.eliminar(nombre, apellido)
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
