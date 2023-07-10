from os import system
system ("cls")

lista=[1,2,3,4,5,6,7,8,9,10,
       11,12,13,14,15,16,17,18,19,20,
       21,22,23,24,25,26,27,28,29,30,
       31,32,33,34,35,36,37,38,39,40,
       41,42,43,44,45,46,47,48,49,50,
       51,52,53,54,55,56,57,58,59,60,
       61,62,63,64,65,66,67,68,69,70,
       71,72,73,74,75,76,77,78,79,80,
       81,82,83,84,85,86,87,88,89,90,
       91,92,93,94,95,96,97,98,99,100] 

asientos=[lista]

def menu():
    print("""Bienvenido, este es nuestro menú: 
    1.- Comprar Entradas 
    2.- Mostrar ubicaciones disponibles
    3.- Ver listado asistentes
    4.- Mostrar ganancias totales
    5.- Salir """)

#Opción 1
def comprar_entradas():
    print("ha seleccionado comprar entradas")
#Opción 2
def asientos_disponibles():
    print("Estos son los asientos disponibles: ")
#Opción 3    
def asistentes():
    print(f"Asistentes ingresados: {rut}")
#Opción 4
def ganancias():
    print("Ha seleccionado ver Ganancias Totales.")
#Opción 5
def salir():
    print("Gracias por su preferencia")

while True:
    menu()
    op=input("Por favor digite una opción: ")
    match op:
        case "1":
            comprar_entradas()
            while True:
                rut=int(input("Por favor, escriba su rut sin guión, puntos ni dígito verificador: \n"))
                if rut < 9999999 and "." in rut and "-" in rut:
                    print("Rut ingresado no válido")
                else:
                    print("Rut ingresado correctamente")
                    break
            platinum=int(input("¿Desea comprar entradas Platinum? digite 0, 1, 2 o 3 dependiendo de cuántas desea llevar. Su precio es de $120.000 \n" ))
            if platinum > 3:
                print("Número ingresado no válido")
            else:
                print(f"Ha comprado {platinum} entrada(s) Platinum")
            gold=int(input("¿Desea comprar entradas Gold? digite 0, 1, 2 o 3 dependiendo de cuántas desea llevar. Su precio es de $80.000 \n"))
            if gold > 3:
                print("Número ingresado no válido")
            else:
                print(f"Ha comprado {gold} entrada(s) Gold")
            silver=int(input("¿Desea comprar entradas Silver? digite 0, 1, 2 o 3 dependiendo de cuántas desea llevar. Su precio es de $50.000 \n"))
            if silver > 3:
                print("Número ingresado no válido")
            else:
                print(f"Ha comprado {silver} entrada(s) Silver")
                pass
        case "2":
            asientos_disponibles()
            print(lista)
            pass
        case "3":
            asistentes()
            pass
        case "4":
            ganancias()
            totalplatinum=platinum*120000
            totalgold=gold*80000
            totalsilver=silver*50000
            total=totalplatinum+totalgold+totalsilver
            print(f"""
            Entradas Platinum compradas: {totalplatinum}
            Entradas Gold compradas:     {totalgold}
            Entradas Silver compradas:   {totalsilver}
                            Total:       {total}""")
            pass
        case "5":
            salir()
            break
        case other:
            print("Seleccione una opción válida")