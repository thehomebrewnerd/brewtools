from brewtools.calculators import correct_gravity


class Gravity():
    """Represents a specific gravity measurement

    Args:
        reading (float): The raw specific gravity reading
        temp (float): The temperature in degrees Fahrenheit of the reading
        cal_temp (float): The calibration temperature of the hydrometer
    """

    def __init__(self, reading=None, temp=None, cal_temp=59):
        self.reading = reading
        self.temp = temp
        self.cal_temp = cal_temp

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}({}, {}, {})".format(class_name,
                                       self.reading,
                                       self.temp,
                                       self.cal_temp)

    def __str__(self):
        unit_str = "F"
        raw_str = "Gravity: {:.3f} at {} deg{}".format(self.raw_value,
                                                       self.temp,
                                                       unit_str)
        corrected_str = "\nCorrected: {:.3f} at {} deg{}".format(self.corrected_value,
                                                                 self.cal_temp,
                                                                 unit_str)
        return raw_str + corrected_str

    @property
    def raw_value(self):
        return self.reading

    @property
    def corrected_value(self):
        return correct_gravity(self.reading, self.temp, self.cal_temp)
