from src.adapter_interface.presenters.modbus_presenter import ModbusPresenter
from src.entities.modbus_reading import ModbusReading
from datetime import datetime


def test_modbus_presenter_to_cli_string():
    reading = ModbusReading(
        timestamp=datetime(2025, 1, 1, 12, 0, 0), registeraddress=7, value=99.9
    )
    output = ModbusPresenter.to_cli_string(reading)
    assert "[2025-01-01 12:00:00] Registro 7: 99.9" in output
