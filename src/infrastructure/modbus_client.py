"""
Path: src/infrastructure/modbus_client.py
"""

import minimalmodbus
import serial
import time

from src.shared.logger_cli_v0 import get_logger


from src.adapter_interface.controllers.modbus_controller import ModbusController
from src.adapter_interface.gateways.modbus_gateway import IModbusGateway
from src.adapter_interface.presenters.modbus_presenter import ModbusPresenter
from src.use_cases.read_modbus_register import ReadModbusRegisterUseCase


class ModbusClientException(Exception):
    "Excepción personalizada para errores del cliente Modbus."

    pass  # pylint: disable=unnecessary-pass


class ModbusClient(IModbusGateway):
    "Cliente Modbus RTU para comunicación con dispositivos Modbus."

    def __init__(
        self,
        port,
        slave_id,
        baudrate=9600,
        parity=serial.PARITY_EVEN,
        stopbits=1,
        timeout=0.5,
    ):
        self.logger = get_logger("modbus-client")
        self.logger.debug(
            "Inicializando ModbusClient con parámetros: "
            "port=%s, slave_id=%s, baudrate=%s, parity=%s, stopbits=%s, timeout=%s",
            port,
            slave_id,
            baudrate,
            parity,
            stopbits,
            timeout,
        )
        try:
            self.instrument = minimalmodbus.Instrument(port, slave_id)
            self.logger.debug(
                "Instrumento minimalmodbus.Instrument creado correctamente."
            )
            self.instrument.serial.baudrate = baudrate
            self.instrument.serial.parity = parity
            self.instrument.serial.stopbits = stopbits
            self.instrument.serial.timeout = timeout
            self.instrument.mode = minimalmodbus.MODE_RTU
            self.logger.info(
                "Instrumento Modbus inicializado en %s con slave ID %s",
                port,
                slave_id,
            )
        except (serial.SerialException, IOError) as e:
            self.logger.error("Error inicializando Modbus: %s", e)
            raise ModbusClientException("Error inicializando Modbus: %s" % e) from e

    def read_register(
        self, registeraddress, number_of_decimals=1, functioncode=3, signed=False
    ):
        "Lee un registro Modbus y devuelve su valor."
        self.logger.debug(
            "Intentando leer registro: address=%s, "
            "number_of_decimals=%s, functioncode=%s, signed=%s",
            registeraddress,
            number_of_decimals,
            functioncode,
            signed,
        )
        try:
            value = self.instrument.read_register(
                registeraddress=registeraddress,
                number_of_decimals=number_of_decimals,
                functioncode=functioncode,
                signed=signed,
            )
            self.logger.info(
                "Lectura exitosa del registro %s: %s",
                registeraddress,
                value,
            )
            self.logger.debug("Valor leído (debug): %s", value)
            if value is None:
                self.logger.warning(
                    "El valor leído del registro %s es None", registeraddress
                )
            return value
        except (serial.SerialException, IOError) as e:
            self.logger.error("Error leyendo registro Modbus: %s", e)
            raise ModbusClientException("Error leyendo registro Modbus: %s" % e) from e
        except Exception as ex:
            self.logger.critical(
                "Excepción crítica leyendo registro %s: %s", registeraddress, ex
            )
            raise


PORT = "COM3"
SLAVE_ID = 1


def main():
    try:
        client = ModbusClient(PORT, SLAVE_ID)
        controller = ModbusController(client)
        use_case = ReadModbusRegisterUseCase(controller)

        while True:
            try:
                reading = use_case.execute(
                    registeraddress=0,
                    number_of_decimals=1,
                    functioncode=3,
                    signed=False,
                )
                print(ModbusPresenter.to_cli_string(reading))
            except ModbusClientException as e:
                print("Error Modbus:", e)
            time.sleep(1)

    except ModbusClientException as e:
        print("Error inicializando el instrumento Modbus:", e)
