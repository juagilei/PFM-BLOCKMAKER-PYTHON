
import json
from web3 import Web3
import os
from dotenv import load_dotenv
from Functions.contractAddressAbi import contractAddressAbi

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Función para la conexión del contrato implementado enla blockchain Ganache:

def conexionContratoEnGanache():
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

# Comprobación de conexión:

    if not web3.is_connected():
        print()
        print("Error: No se pudo conectar a la red Ganache")
        exit()
    else:
        print()
        print("Conexion en Ganache realizada")

    address, abi=contractAddressAbi()

    try:

        contract = web3.eth.contract(address=address, abi=abi)

        # Realizamos alguna acción con el contrato para comprobar que se puede interactuar con él llamando a cualquier función del contrato.

        contract_function = contract.functions.depositarGarantia()
        result = contract_function().call()

        print()
        print("¡Contrato cargado!")
        print()


        # Devolvemos el contrato para futuras operaciones

    except Exception as e:

        print()
        print("Error al conectar con el contrato:", e)
        print()
        exit()

    return contract,web3

def transaccionContrato(web3,tx,key):



    try:

        signed_tx = web3.eth.account.sign_transaction(tx, key) # firma de la transacción.

        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction) # envio de la transacción.

        recibo_tx = web3.eth.wait_for_transaction_receipt(tx_hash)

        return recibo_tx

    except Exception as e:
        raise Exception (f"Error al enviar la transaccion {e}")





