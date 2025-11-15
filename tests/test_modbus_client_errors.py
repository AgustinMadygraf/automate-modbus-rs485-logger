import pytest
from src.infrastructure.modbus_client import ModbusClient, ModbusClientException

class DummyInstrument:
    def __init__(self, raise_on_init=False, raise_on_read=False):
        if raise_on_init:
            raise IOError("Init error")
        self.raise_on_read = raise_on_read
    def read_register(self, *args, **kwargs):
        if self.raise_on_read:
            raise IOError("Read error")
        return 55.5

class DummyLogger:
    def debug(self, *a, **k): pass
    def info(self, *a, **k): pass
    def warning(self, *a, **k): pass
    def error(self, *a, **k): pass
    def critical(self, *a, **k): pass

def test_modbus_client_init_error(monkeypatch):
    monkeypatch.setattr('src.infrastructure.modbus_client.minimalmodbus.Instrument', lambda *a, **k: (_ for _ in ()).throw(IOError("Init error")))
    with pytest.raises(ModbusClientException) as exc:
        ModbusClient('COMX', 1)
    assert "Init error" in str(exc.value)

def test_modbus_client_read_error(monkeypatch):
    class Inst:
        def __init__(self, *a, **k): pass
        def read_register(self, *a, **k): raise IOError("Read error")
        serial = type('serial', (), {})()
        serial.baudrate = 9600
        serial.parity = 0
        serial.stopbits = 1
        serial.timeout = 0.5
        mode = 0
    monkeypatch.setattr('src.infrastructure.modbus_client.minimalmodbus.Instrument', Inst)
    client = ModbusClient('COMX', 1)
    client.instrument = Inst()
    client.logger = DummyLogger()
    with pytest.raises(ModbusClientException) as exc:
        client.read_register(1)
    assert "Read error" in str(exc.value)
