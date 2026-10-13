a = input("Enter Room A status (clean/dirty): ").lower()
b = input("Enter Room B status (clean/dirty): ").lower()
position = input("Enter vacuum position (A/B): ").upper()

if position == "A":
    if a == "dirty":
        print("Cleaning Room A")
    if b == "dirty":
        print("Cleaning Room B")
else:
    if b == "dirty":
        print("Cleaning Room B")
    if a == "dirty":
        print("Cleaning Room A")

print("Both rooms are clean.")
