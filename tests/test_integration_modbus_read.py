"""
Path: tests/test_integration_modbus_read.py
"""

from src.adapter_interface.controllers.modbus_controller import ModbusController
from src.adapter_interface.presenters.modbus_presenter import ModbusPresenter
from src.use_cases.read_modbus_register import ReadModbusRegisterUseCase
from src.infrastructure.modbus_client import ModbusClient
from src.shared.config import get_config


class DummyModbusClient(ModbusClient):
    def __init__(self, *a, **k):
        "Constructor dummy que no inicializa nada."
        pass  # pylint: disable=disabled-method

    def read_register(self, *a, **k):
        return 1234


def test_integration_modbus_read(monkeypatch):
    # Configuración dummy
    config = get_config()
    client = DummyModbusClient()
    controller = ModbusController(client)
    use_case = ReadModbusRegisterUseCase(controller)
    presenter = ModbusPresenter()

    # Simular lectura usando el flujo completo
    reading = use_case.execute(registeraddress=100)
    output = presenter.to_cli_string(reading)

    assert reading.value == 1234
    assert "100" in output
    assert str(reading.value) in output
