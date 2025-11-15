"""
Path: src/adapter_interface/gateways/modbus_gateway.py
"""

from abc import ABC, abstractmethod


class IModbusGateway(ABC):
    "Interfaz para un gateway Modbus."

    @abstractmethod
    def read_register(
        self, registeraddress, number_of_decimals=1, functioncode=3, signed=False
    ):
        "Lee un registro Modbus y devuelve su valor."
        pass  # pylint: disable=unnecessary-pass
