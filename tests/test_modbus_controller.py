import pytest
from unittest.mock import MagicMock
from src.adapter_interface.controllers.modbus_controller import ModbusController
from src.entities.modbus_reading import ModbusReading

class DummyGateway:
    def read_register(self, registeraddress, number_of_decimals=1, functioncode=3, signed=False):
        return 123.0

def test_modbus_controller_read_register():
    gateway = DummyGateway()
    controller = ModbusController(gateway)
    reading = controller.read_register(registeraddress=10)
    assert isinstance(reading, ModbusReading)
    assert reading.registeraddress == 10
    assert reading.value == 123.0
