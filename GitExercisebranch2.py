class digitalConvertor:
    def __init__(self, bitNum, max_voltage):
        self.bitNum = bitNum
        self.max_voltage = max_voltage
        self.max_bits = 2**bitNum - 1

    def convert_voltage(self, input_voltage):
        digital_value = int((input_voltage / self.max_voltage) * self.max_voltage)
        return digital_value
c1 = digitalConvertor(10,5)
input_voltage = 4.5  
res = c1.convert_voltage(input_voltage)
print(f"Digital Value: {res}")
