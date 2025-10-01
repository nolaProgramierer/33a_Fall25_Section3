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


# Grand Pianos


print("\n1) Regular Piano Details:")


print("\n2) Grand Piano Details:")


print("\n3) Play Grand Piano Sound:")


print("\n4) Convert Price to Euros:")


print("\n5) Full Piano Inventory:")


print("\n6) Most Expensive Piano:")


print("\n7) Grand Piano Inventory:")


print("\n8) Pianos with 'Concert Grade':")

