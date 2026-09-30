def power_from_voltage_current(voltage, current):
    power = voltage * current
    return power
def power_from_current_resistance(current, resistance):
    power = current * current * resistance
    return power
def power_from_voltage_resistance(voltage, resistance):
    if resistance == 0:
        return None
    power = voltage * voltage / resistance
    return power