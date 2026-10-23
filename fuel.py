fuel_levels = [15, 30, 8]
for fuel in fuel_levels:
    if fuel < 10:
        print(fuel, "CRITICAL, refuel now")
    elif fuel < 20:
        print(fuel, "fuel is drying")
    else:
        print(fuel, "fuel is ok")