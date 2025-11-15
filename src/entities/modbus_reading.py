"""
Path: src/entities/modbus_reading.py
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class ModbusReading:
    "Data class representing a Modbus reading."
    timestamp: datetime
    registeraddress: int
    value: float
