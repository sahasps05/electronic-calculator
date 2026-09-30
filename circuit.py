def series_circuit(r1, r2, r3):
    total = r1 + r2 + r3
    return total
def parallel_circuit(r1, r2, r3):
    if r1 == 0 or r2 == 0 or r3 == 0:
        return None
    total = 1 / ((1 / r1) + (1 / r2) + (1 / r3))
    return total