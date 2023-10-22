class digitalConvertor:
    def __init__(self, resolution=10, reference_voltage=5.0):
        self.resolution = resolution
        self.reference_voltage = reference_voltage
        self.max_value = 2**resolution - 1

    def convert_voltage(self, input_voltage):
        digital_value = int((input_voltage / self.reference_voltage) * self.max_value)
        return digital_value
c1 = digitalConvertor()
input_voltage = 4.5  
res = c1.convert_voltage(input_voltage)
print(f"Digital Value: {res}")
