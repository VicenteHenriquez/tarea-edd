# -*- coding: utf-8 -*-
if __name__=="__main__":
    import listacontactosterminada as ldct
    import hashcontactos as hdc
    import arbolcontactos as ac
    import arbol23contacto as adtc
    print("Bienvenido/a a su agenda personal. ")
    print("Escoja el modo de agenda que desee: ")
    print("1.Lista")
    print("2.Arbol de busqueda")
    print("3.Arbol 2-3")
    print("4.Hash")
    aux = input()
    if aux == 1:
        ldct.main()
    elif aux == 2:
        ac.main()
    elif aux == 3:
        adct.main()
    elif aux == 4:
        hdc.main()
    else:
        print("No existe esta operacion.")                
