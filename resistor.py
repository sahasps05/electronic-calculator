def series_resistance(r1, r2):
    total = r1 + r2
    return total
def parallel_resistance(r1, r2):
    if r1 + r2 == 0:
        return None
    total = (r1 * r2) / (r1 + r2)
    return total