# ohms_law.py
# Simple Ohm's Law calculator: V = I * R
# Name: Peter Ntima Anya
# Assignment: PySphere Python Project 101 - Ohm's Law Voltage Calculator
# Date: 12 August 2025

# Ask for current in amperes
current = float(input("Enter current (A): "))

# Ask for resistance in ohms
resistance = float(input("Enter resistance (Ω): "))

# Calculate voltage
voltage = current * resistance

print(f"Voltage (V) = {voltage} volts")
