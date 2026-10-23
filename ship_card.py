fleet = [
    {"name": "hari", "fuel": 34},
    {"name": "nehemiah", "fuel": 35},
    {"name": "nehemiah hari", "fuel": 66},
]
for ship in fleet:
    if ship["fuel"] < 40:
        print(ship["name"], "LOW FUEL")
    else:
        print(ship["name"], "OK")