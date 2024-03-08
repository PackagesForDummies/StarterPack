"""Temperature conversions"""

def C2F(tempC:float) -> float:
    """Converts a temperature in °C to °F"""
    return 32.0 + 1.8 * tempC

def F2C(tempF:float) -> float:
    """Converts a temperature in °F to °C"""
    return (tempF - 32.0) / 1.8
