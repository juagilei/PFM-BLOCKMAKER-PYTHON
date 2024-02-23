# Uso getpass para introducir cleves personales
import getpass
from Functions.menuPrincipal import *
from Functions.funcionesContrato import *
from Functions.funcionesWeb3Ganache import conexionContratoEnGanache

def main ():

    while True:

        menuPrincipal()

        opcion = input("\033[1;32mIntroduce la opción deseada: \033[m")

        if opcion == "1":
            print()
            nuevo_prestamista_address = input("Introduce la dirección del prestamista para darlo de alta: ")
            altaPretamista(nuevo_prestamista_address)
            print()

        elif opcion == "2":
            print()
            nuevo_cliente_address = input("Introduce la dirección del cliente: ")
            print()
            prestamista_address = input("Introduce tu dirección como prestamista: ")
            print()

    # Uso getpass para introducir datos sensibles y que no se vean

            prestamista_key = getpass.getpass(prompt="Ingresa tu llave privada: ")
            print()

            altaCliente(nuevo_cliente_address, prestamista_address, prestamista_key)

        elif opcion == "3":
            print()
            cliente = input("Introduce la dirección del cliente: ")
            print()
            monto_garantia = int(input("Deposita el monto en Ether correspondoiente a la garantía del prestamo: "))
            print()
            key_cliente = getpass.getpass(prompt="Ingresa tu llave privada: ")
            print()

            depositarGarantia(cliente, key_cliente, monto_garantia)

        elif opcion == "4":
             print()
             cliente_address = input("Introduce la dirección del cliente: ")
             print()
             cliente_key = getpass.getpass(prompt="Ingresa tu llave privada del cliente: ")
             print()
             monto_prestamo = int(input("Introduce el monto a solicitar: "))
             print()
             plazo_prestamo = int(input("Introduce el plazo a pagar el prestamo: "))

             solicitarPrestamos(monto_prestamo, plazo_prestamo, cliente_address, cliente_key)
        
        elif opcion == "5":
           
            print()
            cliente = input("introduce la direccion del cliente: ")
            id_prestamo = int(input("Introduce el identificador del prestamo: "))
            prestamista_address = input("Introduce la dirección del prestamista: ")
            prestamista_key = getpass.getpass(prompt="Ingresa la llave privada del prestamista: ")


            aprobarPrestamo(cliente, id_prestamo, prestamista_address, prestamista_key)

        elif opcion == "6":
            print()
            id_prestamo = int(input("Introduce el identificador del prestamo: "))
            cliente_address = input("introduce la dirección del cliente: ")
            cliente_key = getpass.getpass(prompt="Introduce la clave del cliente: ")


            reembolsarPrestamo(id_prestamo, cliente_address, cliente_key)

        elif opcion == "7":

            print()
            cliente_address = input("introduce la dirección del cliente: ")
            id_prestamo = int(input("Introduce el identificador del prestamo: "))
            prestamista_address = input("introdice la dirección del prestamista: ")
            prestamista_key = getpass.getpass(prompt="Introduce la clave del prestamista: ")


            liquidarGrantia (cliente_address, id_prestamo, prestamista_address, prestamista_key)

        elif  opcion == "8":
            print()
            cliente_address = input ("Introduce la dirección del cliente: ")
            print()
            obtenerPrestamosPorPrestatario(cliente_address)

        elif  opcion == "9":
            print()
            cliente_address = input("Introduce la direccion del cliente: ")
            id_prestamo = int(input("Introduce el identificador del prestamo: "))


            obtenerDetallaPrestamo(cliente_address, id_prestamo )

        elif  opcion == "0":
            print("saliendo del menú")
            break
        else :
            print("Error, elige una de las opcines.")

conexionContratoEnGanache()

main()



