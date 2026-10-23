ship = {"name" : "Ocean Star", "imo" : 9360628, "fuel" : 25}
ship["name"] = "hari"
print(ship["imo"])
print(ship["fuel"])  
ship["fuel" ] = 10

print(ship)
cricket = {"batsman" : "hari", "bowling" : 4, "fielder" : "nehemiah"}
print(cricket["batsman"])
print(cricket["fielder"])

ship = {"name": "Ocean Star", "imo": 9360628, "fuel": 25}
ship["name"] = "hari"
print(ship["imo"])
print(ship["fuel"])
ship["fuel"] = 10
print(ship)

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