from src.use_cases.read_modbus_register import ReadModbusRegisterUseCase
from src.entities.modbus_reading import ModbusReading

class DummyController:
    def read_register(self, registeraddress, number_of_decimals=1, functioncode=3, signed=False):
        return ModbusReading(timestamp=None, registeraddress=registeraddress, value=42.0)

def test_read_modbus_register_use_case():
    controller = DummyController()
    use_case = ReadModbusRegisterUseCase(controller)
    reading = use_case.execute(registeraddress=5)
    assert isinstance(reading, ModbusReading)
    assert reading.registeraddress == 5
    assert reading.value == 42.0
