from enum import Enum

# Size enumeration
class Size(Enum):
    SMALL = 1.50
    MEDIUM = 1.75
    LARGE = 2.05
    MEGA = 2.15

# Flavor enumeration (extra credit)
class Flavor(Enum):
    LEMON = 0.15
    VANILLA = 0.15
    CHOCOLATE = 0.15
    STRAWBERRY = 0.15

class Drink:
    def __init__(self, base, flavor, size):
        self.base = base
        self.flavor = flavor
        self.size = size.lower()  # Case-insensitive size handling

    def cost(self):
        base_cost = Size[self.size.upper()].value
        flavor_cost = Flavor[self.flavor.upper()].value if self.flavor else 0.0
        return base_cost + flavor_cost

    # Extra credit: Custom format for printing
    def __str__(self):
        return f"Drink('{self.base}', flavor='{self.flavor}', size='{self.size}')"

class Order:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def calculate_total(self):
        total = sum(drink.cost() for drink in self.drinks)
        return total + (total * 0.0725)  # Adding 7.25% tax

    def generate_receipt(self):
        receipt = []
        for i, drink in enumerate(self.drinks, start=1):
            receipt.append(f"Drink {i}: {drink.base} ({drink.size.capitalize()}, {drink.flavor.capitalize()}) - Cost: ${drink.cost():.2f}")

        total = self.calculate_total()
        receipt.append(f"\nTotal Beverages: {len(self.drinks)}")
        receipt.append(f"Order Total: ${total:.2f} (Including 7.25% tax)")

        # Return raw data instead of using print
        return "\n".join(receipt)

# Example usage:
order = Order()
order.add_drink(Drink('hill fog', 'lemon', 'medium'))
order.add_drink(Drink('mr. salt', 'vanilla', 'large'))

# Retrieve the order receipt as raw data
order_receipt = order.generate_receipt()
print(order_receipt)

# Extra credit: Custom format for printing
drink = Drink('hill fog', 'lemon', 'medium')
print(drink)

# Extra credit: Live calculation of the total cost
live_calculated_cost = Drink('mr. salt', 'vanilla', 'large').cost()
print(f"Live Calculated Cost: ${live_calculated_cost:.2f}")
