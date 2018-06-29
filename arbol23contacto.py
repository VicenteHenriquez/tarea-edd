# -*- coding: utf-8 -*-
class nodo:
    def __init__(self, nombre, apellido, telefono, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail

class node:
    def __init__(self, nodo):
        self.data = [nodo]
        self.parent = None
        self.child = []

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + " : " + str(self.data)
        return "Root: " + str(self.data)

    def _is_leaf(self):
        return len(self.child) == 0

    def _add(self, new_node):
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()

    def _insert(self, new_node):
        if self._is_leaf():
            self._add(new_node)
        elif new_node.data[0] < self.data[-1]:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] < self.data[i]:
                    self.child[i]._insert(new_node)
                    break

    def _split(self):
        left_child = node(self.data[1], self)
        right_child = node(self.data[2], self)
        if self.child:
        	self.child[0].parent = left_child
        	self.child[1].parent = left_child
        	self.child[2].parent = right_child
        	self.child[3].parent = right_child
        	left_child.child = [self.child[0], self.child[1]]
        	right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        # Ahora tenemos un nuevo sub-arbol, y necesitamos añadirlo a su nodo padre
        if self.parent:
        	if self in self.parent.child:
        		self.parent.child.remove(self)
        	self.parent._add(self)
        else:
        	left_child.parent = self
        	right_child.parent = self

    def _find(self, apellido):
    	if apellido in self.data.apellido:
    		return nodo.apellido and nodo.nombre and nodo.telefono and nodo.mail
    	elif self._is_leaf():
    		return False
    	elif apellido > self.data[-1].apellido:
    		return self.child[-1]._find(apellido)
    	else:
    		for i in range(len(self.data)):
    			if item < self.data[i]:
    				return self.child[i]._find(apellido)

    def _preorder(self):
    	print(self)
    	for child in self.child:
            child._preorder()

class Tree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def insert(self, nombre, apellido, telefono, mail):
        nodo1 = nodo(nombre, apellido, telefono, mail)
        if self.empty():
            self.root = node(nodo1)
        else:
            self.root._insert(node(nodo1))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def find(self, apellido):
        return self.root._find(apellido)

    def pre_order(self):
        self.root._preorder()

def main():
    while True:
        print("Seleccione una opcion: ")
        print("1.Agregar contacto")
        print("2.Buscar contacto")
        print("3.Ver lista completa")
        aux = input()
        ldc = Tree()
        if aux == 1:
            print("Ingrese nombre: ")
            nombre = input()
            print("apellido: ")
            apellido = input()
            print("telefono: ")
            telefono = input()
            print("mail: ")
            mail = input()
            ldc.insert(nombre, apellido, telefono, mail)
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
            ldc.find(apellido)
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        elif aux == 3:
            print("Imprimiendo lista de contactos: ")
            ldc.pre_order()
            print("¿Desea otra operacion? ")
            resp = input()
            if resp == "si":
                pass
            else:
                break
        else:
            print("Buen dia")
            break
