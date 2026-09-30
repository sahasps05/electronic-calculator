def find_voltage(current, resistance):
    voltage = current * resistance
    return voltage
def find_current(voltage, resistance):
    if resistance == 0:
        return None
    current = voltage / resistance
    return current
def find_resistance(voltage, current):
    if current == 0:
        return None
    resistance = voltage / current
    return resistance