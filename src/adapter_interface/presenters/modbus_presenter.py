"""
Path: src/adapter_interface/presenters/modbus_presenter.py
"""

from src.entities.modbus_reading import ModbusReading


class ModbusPresenter:
    "Presenter para formatear lecturas Modbus."

    @staticmethod
    def to_cli_string(reading: ModbusReading) -> str:
        "Formatea una lectura Modbus para salida en CLI."
        return (
            f"[{reading.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Registro {reading.registeraddress}: {reading.value}"
        )
