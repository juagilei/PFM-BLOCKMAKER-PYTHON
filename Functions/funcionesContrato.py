
import json
import os
from dotenv import load_dotenv
from web3 import Web3
from Functions.funcionesWeb3Ganache import *


def altaPretamista(nuevo_prestamista_address):

    socio_principal_address = os.getenv("SOCIO_PRINCIPAL_ADDRESS")
    socio_principal_key = os.getenv("SOCIO_PRINCIPAL_KEY")
    contract,web3 = conexionContratoEnGanache()
    key = socio_principal_key

    # Preparando la transacción en tx:
    # Aseguramos que no existan duplicados de transacciones, esta trasaccion es única

    nonce = web3.eth.get_transaction_count(socio_principal_address)

    # En la transacción llamo a la función del contrato y la introduzco los datos recogidos en esta función ("alta_pretamista(nuevo_prestamista_address"))

    tx = contract.functions.altaPrestamista(nuevo_prestamista_address).build_transaction({
        'from': socio_principal_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print("El pretamista ha sido dado de alta")

def altaCliente(nuevo_cliente_address, prestamista_address, prestamista_key):

    contract,web3 = conexionContratoEnGanache()
    key = prestamista_key

    nonce = web3.eth.get_transaction_count(prestamista_address)

    tx = contract.functions.altaCliente(nuevo_cliente_address).build_transaction({
        'from': prestamista_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print("El cliente ha sido dado de alta")

def depositarGarantia(cliente_address, cliente_key, monto_garantia):

    contract,web3 = conexionContratoEnGanache()
    key = cliente_key

    nonce = web3.eth.get_transaction_count(cliente_address)

    monto = web3.to_wei(monto_garantia, 'ether')

    tx = contract.functions.depositarGarantia().build_transaction({
        'from': cliente_address,
        'nonce': nonce,
        'gas': 100000,
        'value': monto,
        'gasPrice': web3.to_wei('50', 'gwei')

    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print(f"Se han depositado {monto_garantia} Ether como garantia del prestamo")

def solicitarPrestamos (monto_prestamo, plazo_prestamo, cliente_address, cliente_key):

    contract,web3 = conexionContratoEnGanache()
    key = cliente_key

    nonce = web3.eth.get_transaction_count(cliente_address)

    tx = contract.functions.solicitarPrestamos(monto_prestamo, plazo_prestamo).build_transaction({
        'from': cliente_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    recibo=transaccionContrato(web3,tx,key)

    prestamoId=contract.functions.solicitarPrestamos(monto_prestamo, plazo_prestamo).call()

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print(f"Se ha solicitado el prestamo con el ID: {prestamoId}")

def aprobarPrestamo(cliente, id_prestamo, prestamista_address, prestamista_key ):

    contract,web3 = conexionContratoEnGanache()
    key = prestamista_key

    nonce = web3.eth.get_transaction_count(prestamista_address)

    tx = contract.functions.aprobarPrestamo(cliente, id_prestamo).build_transaction({
        'from': prestamista_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')

    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print(f"Prestamo con ID: {id_prestamo} aprobado")

def  reembolsarPrestamo(id_prestamo, cliente_address, cliente_key):

    contract,web3 = conexionContratoEnGanache()
    key = cliente_key

    nonce = web3.eth.get_transaction_count(cliente_address)

    tx = contract.functions.reembolsarPrestamo(id_prestamo).build_transaction({
        'from': cliente_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')

    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print(f"Prestamo con ID: {id_prestamo} reembolsado")

def liquidarGrantia (cliente_address, id_prestamo, prestamista_address, prestamista_key):

    contract,web3 = conexionContratoEnGanache()
    key = prestamista_key
    nonce = web3.eth.get_transaction_count(prestamista_address)

    tx = contract.functions.liquidarGrantia (cliente_address, id_prestamo).build_transaction({
        'from': prestamista_address,
        'nonce': nonce,
        'gas': 100000,
        'gasPrice': web3.to_wei('50', 'gwei')

    })

    recibo=transaccionContrato(web3,tx,key)

    print(f'Transacion realizada con exito. Hash: {recibo.transactionHash.hex()}')
    print()
    print(f"Prestamo con ID: {id_prestamo} a sido liquidado")

def obtenerPrestamosPorPrestatario(cliente_address):

    contract,web3 = conexionContratoEnGanache()

    resultado = contract.functions.obtenerPrestamosPorPrestatario(cliente_address).call()

    print(f"Los prestamos del cliente son: {resultado}")

def  obtenerDetallaPrestamo(cliente_address, id_prestamo ):

    contract,web3 = conexionContratoEnGanache()

    resultado = contract.functions.obtenerDetallaPrestamo(cliente_address, id_prestamo ).call()
    print()
    print(f"El detalle del prestamo es: ")
    print()
    print(f"Identificador: {resultado[0]}")
    print(f"Prestatario; {resultado[1]}")
    print(f"Monto: {resultado[2]} Ether")
    print(f"Plazo: {resultado[3]}")
    print(f"Tiempo de la solicitud: {resultado[4]}")
    print(f"Tiempo límite: {resultado[5]}")
    print(f"Aprobado: {resultado[6]}")
    print(f"Reembolsado: {resultado[7]}")
    print(f"Liquidado: {resultado[8]}")



