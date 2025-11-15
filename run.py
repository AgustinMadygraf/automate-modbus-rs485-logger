"""
Path: run.py
"""

import time
from src.infrastructure.modbus_client import ModbusClient, ModbusClientException

PORT = 'COM3'
SLAVE_ID = 1

try:
    client = ModbusClient(PORT, SLAVE_ID)

    while True:
        try:
            raw_value = client.read_register(
                registeraddress=0,
                number_of_decimals=1,
                functioncode=3,
                signed=False
            )
            print("Valor leído:", raw_value)
        except ModbusClientException as e:
            print("Error Modbus:", e)
        time.sleep(1)

except ModbusClientException as e:
    print("Error inicializando el instrumento Modbus:", e)
