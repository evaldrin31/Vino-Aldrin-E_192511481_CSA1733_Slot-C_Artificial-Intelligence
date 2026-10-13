# Vacuum Cleaner Problem

room_a = input("Enter status of Room A (Clean/Dirty): ").lower()
room_b = input("Enter status of Room B (Clean/Dirty): ").lower()
location = input("Enter vacuum location (A/B): ").upper()

rooms = {"A": room_a, "B": room_b}

for room in ["A", "B"]:
    if rooms[location] == "dirty":
        print("Cleaning Room", location)
        rooms[location] = "clean"
    else:
        print("Room", location, "is already clean")

    location = "B" if location == "A" else "A"

print("Both rooms are clean.")
