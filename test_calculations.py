import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ohms_law import find_voltage, find_current, find_resistance
from power import power_from_voltage_current
from resistor import series_resistance, parallel_resistance
def test_ohms_law():
    assert find_voltage(5, 10) == 50
    assert find_current(50, 10) == 5
    assert find_resistance(50, 5) == 10
def test_power():
    assert power_from_voltage_current(10, 2) == 20
def test_series_resistance():
    assert series_resistance(10, 20) == 30
def test_parallel_resistance():
    assert parallel_resistance(10, 10) == 5
print("All tests passed successfully.")