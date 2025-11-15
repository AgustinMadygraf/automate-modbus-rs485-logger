"""
Path: src/use_cases/read_modbus_register.py
"""

from src.adapter_interface.controllers.modbus_controller import ModbusController
from src.entities.modbus_reading import ModbusReading

class ReadModbusRegisterUseCase:
    "Caso de uso para leer un registro Modbus."
    def __init__(self, controller: ModbusController):
        self.controller = controller

    def execute(self, registeraddress, number_of_decimals=1, functioncode=3, signed=False) -> ModbusReading:
        "Lee un registro Modbus y devuelve la lectura."
        return self.controller.read_register(
            registeraddress=registeraddress,
            number_of_decimals=number_of_decimals,
            functioncode=functioncode,
            signed=signed
        )
    
