# ohms_law.py
# Simple Ohm's Law calculator: V = I * R

# Ask for current in amperes
current = float(input("Enter current (A): "))

# Ask for resistance in ohms
resistance = float(input("Enter resistance (Ω): "))

# Calculate voltage
voltage = current * resistance

print(f"Voltage (V) = {voltage} volts")
