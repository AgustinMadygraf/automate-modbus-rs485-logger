"""
Path: src/adapter_interface/controllers/modbus_controller.py
"""

from datetime import datetime

from src.adapter_interface.gateways.modbus_gateway import IModbusGateway
from src.entities.modbus_reading import ModbusReading

class ModbusController:
    "Controller para operaciones Modbus."
    def __init__(self, modbus_gateway: IModbusGateway):
        self.modbus_gateway = modbus_gateway

    def read_register(self, registeraddress, number_of_decimals=1, functioncode=3, signed=False):
        "Lee un registro usando el gateway y devuelve una entidad ModbusReading."
        value = self.modbus_gateway.read_register(
            registeraddress=registeraddress,
            number_of_decimals=number_of_decimals,
            functioncode=functioncode,
            signed=signed
        )
        return ModbusReading(
            timestamp=datetime.now(),
            registeraddress=registeraddress,
            value=value
        )
