#Daily Python Project
#Day 1
#Weather Temp Converter

temperatures_fahrenheit = [32, 50, 77, 100, 212]

celsius = [(f - 32) * 5.0/9.0 for f in temperatures_fahrenheit]

print("Temperatures in Fahrenheit: ", temperatures_fahrenheit)
print("Temperatures in Celsius: ", celsius)