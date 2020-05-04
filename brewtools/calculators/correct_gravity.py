def correct_gravity(sg, temp, cal_temp):
    """Correct a specific gravity reading to the specified calibration temperature

    Args:
        sg (float): Measured specific gravity
        temp (float): Measurement temperature in degrees Fahrenheit
        cal_temp (float): Hydrometer calibration temperature in degrees Fahrenheit
    """

    numerator = 1.00130346 - 0.000134722124 * temp + 0.00000204052596 * temp**2 - 0.00000000232820948 * temp**3
    denom = 1.00130346 - 0.000134722124 * cal_temp + 0.00000204052596 * cal_temp**2 - 0.00000000232820948 * cal_temp**3
    corrected_gravity = sg * numerator / denom
    return corrected_gravity
