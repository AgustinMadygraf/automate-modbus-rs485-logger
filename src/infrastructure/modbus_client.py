"""
Path: src/infrastructure/modbus_client.py
"""


import minimalmodbus
import serial

from src.shared.logger_cli_v0 import get_logger

class ModbusClientException(Exception):
    "Excepción personalizada para errores del cliente Modbus."
    pass # pylint: disable=unnecessary-pass


class ModbusClient:
    "Cliente Modbus RTU para comunicación con dispositivos Modbus."
    def __init__(self, port, slave_id, baudrate=9600, parity=serial.PARITY_EVEN, stopbits=1, timeout=0.5):
        self.logger = get_logger("modbus-client")
        try:
            self.instrument = minimalmodbus.Instrument(port, slave_id)
            self.instrument.serial.baudrate = baudrate
            self.instrument.serial.parity = parity
            self.instrument.serial.stopbits = stopbits
            self.instrument.serial.timeout = timeout
            self.instrument.mode = minimalmodbus.MODE_RTU
            self.logger.info("Instrumento Modbus inicializado en %s con slave ID %s", port, slave_id)
        except (serial.SerialException, IOError) as e:
            raise ModbusClientException("Error inicializando Modbus: %s" % e) from e

    def read_register(self, registeraddress, number_of_decimals=1, functioncode=3, signed=False):
        "Lee un registro Modbus y devuelve su valor."
        try:
            value = self.instrument.read_register(
                registeraddress=registeraddress,
                number_of_decimals=number_of_decimals,
                functioncode=functioncode,
                signed=signed
            )
            self.logger.debug("Leído registro %s: %s", registeraddress, value)
            return value
        except (serial.SerialException, IOError) as e:
            raise ModbusClientException("Error leyendo registro Modbus: %s" % e) from e
