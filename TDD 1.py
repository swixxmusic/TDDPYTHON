class Drink:
    def __init__(self, base):
        self._base = base
        self._flavors = []

    def get_flavors(self):
        return self._flavors

    def get_base(self):
        return self._base

    def get_total(self):
        return 1 + len(self._flavors)

    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, flavors):
        # Ensure no duplicate flavors
        unique_flavors = set(flavors)
        self._flavors = list(unique_flavors)

    def add_flavor(self, flavor):
        if flavor not in self._flavors:
            self._flavors.append(flavor)


class Order:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(item.get_total() for item in self._items)

    def add_item(self, drink):
        self._items.append(drink)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]


# Valid bases and flavors
valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

# Example usage
order = Order()

drink1 = Drink('water')
drink1.set_flavors(['lemon', 'mint'])
order.add_item(drink1)

drink2 = Drink('pokeacola')
drink2.add_flavor('cherry')
order.add_item(drink2)

# Accessing information
for i, item in enumerate(order.get_items()):
    print(f"Item {i + 1}: Base - {item.get_base()}, Flavors - {item.get_flavors()}, Total - {item.get_total()}")

print(f"Total items in order: {order.get_num_items()}")
print(f"Total cost of order: ${order.get_total()}")
