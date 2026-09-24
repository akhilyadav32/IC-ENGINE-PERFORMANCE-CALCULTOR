import math


def brake_power(torque, rpm):
    bp = (2 * math.pi * torque * rpm) / (60 * 1000)
    return bp



def indicated_power():
    ip = float(input("Enter Indicated Power (kW): "))
    return ip



def friction_power(ip, bp):
    fp = ip - bp
    return fp



def mechanical_efficiency(bp, ip):
    efficiency = (bp / ip) * 100
    return

while True:

    print("\n===== IC ENGINE PERFORMANCE CALCULATOR =====")
    print("1. Calculate Brake Power")
    print("2. Calculate Indicated Power")
    print("3. Calculate Friction Power")
    print("4. Calculate Mechanical Efficiency")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        torque = float(input("Enter Torque (N-m): "))
        rpm = float(input("Enter Engine Speed (RPM): "))

        bp = brake_power(torque, rpm)

        print("Brake Power =", round(bp, 2), "kW")

    elif choice == 2:
        ip = indicated_power()

        print("Indicated Power =", round(ip, 2), "kW")

    elif choice == 3:
        ip = float(input("Enter Indicated Power (kW): "))
        bp = float(input("Enter Brake Power (kW): "))

        if ip >= bp:
            fp = friction_power(ip, bp)
            print("Friction Power =", round(fp, 2), "kW")
        else:
            print("Error: Indicated Power must be greater than or equal to Brake Power.")

    elif choice == 4:
        ip = float(input("Enter Indicated Power (kW): "))
        bp = float(input("Enter Brake Power (kW): "))

        if ip > 0 and bp >= 0 and bp <= ip:
            efficiency = mechanical_efficiency(bp, ip)
            print("Mechanical Efficiency =", round(efficiency, 2), "%")
        else:
            print("Error: Enter valid power values.")

    elif choice == 5:
        print("Thank you for using the IC Engine Calculator!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
