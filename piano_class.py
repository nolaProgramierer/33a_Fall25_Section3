class Piano:
    inventory = []  # Stores all instances

    def __init__(self, brand, price, keys=88, pedals=3, features=None):
        self.brand = brand
        self.price = price
        self.keys = keys
        self.pedals = pedals
        self.features = features if features is not None else []
        Piano.inventory.append(self)

    # Instance methods used in demo
    def print_piano_details(self):
        print(f"{self.brand} - ${self.price:,.0f}")
        print(f"Features: {', '.join(self.features)}")

    def convert_price_to_euros(self, rate):
        return self.price * rate

    # Class methods used in demo
    @classmethod
    def get_inventory(cls):
        return cls.inventory

    @classmethod
    def get_most_expensive_piano(cls):
        if not cls.inventory:
            return None
        return max(cls.inventory, key=lambda piano: piano.price)

    @classmethod
    def find_piano_by_feature(cls, feature):
        return [piano for piano in cls.inventory if feature in piano.features]


class GrandPiano(Piano):
    inventory = []  # Separate inventory for Grand Pianos

    def __init__(self, brand, price, size, keys=88, features=None):
        super().__init__(brand, price, keys=keys, features=features)
        self.size = size
        GrandPiano.inventory.append(self)

    def print_piano_details(self):
        super().print_piano_details()
        print(f"Size: {self.size}")

    def play_sound(self):
        print("Playing a beautiful, rich, singing grand piano sound")


# -----------------------------
# Demo
# -----------------------------
# Regular Pianos
p1 = Piano("Yamaha", 5000, features=["Silent Mode"])
p2 = Piano("Steinway", 12000, features=["Concert Grade"])
p3 = Piano("Kawai", 7000, features=["Hybrid Action"])

# Grand Pianos
g1 = GrandPiano("Bösendorfer", 150000, "9ft", keys=97, features=["Handcrafted", "Limited Edition", "Concert Grade"])
g2 = GrandPiano("Steinway", 90000, "7ft", features=["Concert Hall Quality"])
g3 = GrandPiano("Yamaha", 45000, "6ft", features=["Player System"])

print("\n1) Regular Piano Details:")
p1.print_piano_details()

print("\n2) Grand Piano Details:")
g2.print_piano_details()

print("\n3) Play Grand Piano Sound:")
g3.play_sound()

print("\n4) Convert Price to Euros:")
euro_price = g2.convert_price_to_euros(1.09)
print(f"The price in euros for the {g2.brand} is €{euro_price:,.0f}")

print("\n5) Full Piano Inventory:")
for piano in Piano.get_inventory():
    print(f"{piano.brand} - ${piano.price:,.0f}")

print("\n6) Most Expensive Piano:")
expensive = Piano.get_most_expensive_piano()
print(f"{expensive.brand} is the most expensive piano in inventory.")

print("\n7) Grand Piano Inventory:")
for grand in GrandPiano.get_inventory():
    print(f"{grand.brand} - ${grand.price:,.0f}")

print("\n8) Pianos with 'Concert Grade':")
for piano in Piano.find_piano_by_feature("Concert Grade"):
    print(f"{piano.brand} - ${piano.price:,.0f} - Features: {', '.join(piano.features)}")
