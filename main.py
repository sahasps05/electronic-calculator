from ohms_law import find_voltage, find_current, find_resistance
from power import power_from_voltage_current,power_from_current_resistance,power_from_voltage_resistance
from resistor import series_resistance, parallel_resistance
from circuit import series_circuit, parallel_circuit
def get_number(message):
    while True:
        try:
            number = float(input(message))
            if number < 0:
                print("Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number.")
def ohms_law_menu():
    print("\n--- Ohm's Law ---")
    print("1. Find Voltage")
    print("2. Find Current")
    print("3. Find Resistance")
    choice = input("Enter your choice: ")
    if choice == "1":
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (ohm): ")
        voltage = find_voltage(current, resistance)
        print("Voltage =", voltage, "V")
    elif choice == "2":
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (ohm): ")
        if resistance == 0:
            print("Resistance cannot be zero.")
        else:
            current = find_current(voltage, resistance)
            print("Current =", current, "A")
    elif choice == "3":
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")
        if current == 0:
            print("Current cannot be zero.")
        else:
            resistance = find_resistance(voltage, current)
            print("Resistance =", resistance, "ohm")
    else:
        print("Invalid choice.")
def power_menu():
    print("\n--- Power Calculator ---")
    print("1. Using Voltage and Current")
    print("2. Using Current and Resistance")
    print("3. Using Voltage and Resistance")
    choice = input("Enter your choice: ")
    if choice == "1":
        voltage = get_number("Enter voltage (V): ")
        current = get_number("Enter current (A): ")
        power = power_from_voltage_current(voltage, current)
        print("Power =", power, "W")
    elif choice == "2":
        current = get_number("Enter current (A): ")
        resistance = get_number("Enter resistance (ohm): ")
        power = power_from_current_resistance(current, resistance)
        print("Power =", power, "W")
    elif choice == "3":
        voltage = get_number("Enter voltage (V): ")
        resistance = get_number("Enter resistance (ohm): ")
        if resistance == 0:
            print("Resistance cannot be zero.")
        else:
            power = power_from_voltage_resistance(voltage, resistance)
            print("Power =", power, "W")
    else:
        print("Invalid choice.")
def resistor_menu():
    print("\n--- Resistor Calculator ---")
    print("1. Series")
    print("2. Parallel")
    choice = input("Enter your choice: ")
    if choice == "1":
        r1 = get_number("Enter R1: ")
        r2 = get_number("Enter R2: ")
        total = series_resistance(r1, r2)
        print("Total Resistance =", total, "ohm")
    elif choice == "2":
        r1 = get_number("Enter R1: ")
        r2 = get_number("Enter R2: ")
        if r1 == 0 or r2 == 0:
            print("Resistance cannot be zero.")
        else:
            total = parallel_resistance(r1, r2)
            print("Total Resistance =", total, "ohm")
    else:
        print("Invalid choice.")
def circuit_menu():
    print("\n--- Circuit Calculator ---")
    print("1. Series Circuit")
    print("2. Parallel Circuit")
    choice = input("Enter your choice: ")
    if choice == "1":
        r1 = get_number("Enter R1: ")
        r2 = get_number("Enter R2: ")
        r3 = get_number("Enter R3: ")
        total = series_circuit(r1, r2, r3)
        print("Total Resistance =", total, "ohm")
    elif choice == "2":
        r1 = get_number("Enter R1: ")
        r2 = get_number("Enter R2: ")
        r3 = get_number("Enter R3: ")
        if r1 == 0 or r2 == 0 or r3 == 0:
            print("Resistance cannot be zero.")
        else:
            total = parallel_circuit(r1, r2, r3)
            print("Total Resistance =", total, "ohm")
    else:
        print("Invalid choice.")
while True:
    print("\n==============================")
    print("     ELECTRONIC CALCULATOR")
    print("==============================")
    print("1. Ohm's Law")
    print("2. Power Calculator")
    print("3. Resistor Calculator")
    print("4. Circuit Calculator")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ohms_law_menu()
    elif choice == "2":
        power_menu()
    elif choice == "3":
        resistor_menu()
    elif choice == "4":
        circuit_menu()
    elif choice == "5":
        print("Thank you for using Electronic Calculator.")
        break
    else:
        print("Invalid choice. Please try again.")