# api/ice_cream.py
class IceCream:
    def __init__(self):
        self.flavors = []
        self.mix_ins = []

    def get_flavors(self):
        return self.flavors

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def get_base(self):
        return "Ice Cream"

    def get_total(self):
        total = 0
        for flavor in self.flavors:
            total += flavor.cost
        for mix_in in self.mix_ins:
            total += mix_in.cost
        return total

    def get_num_flavors(self):
        return len(self.flavors)

    def __str__(self):
        return f"Ice Cream: {', '.join(flavor.name for flavor in self.flavors)}"

# api/mix_ins.py
class MixIn:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# api/order.py
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_total()
        return total

    def __str__(self):
        return f"Order Total: ${self.get_total()}"

# tests/test_ice_cream.py
import unittest
from api.ice_cream import IceCream
from api.mix_ins import MixIn

class TestIceCream(unittest.TestCase):
    def test_add_flavor(self):
        ice_cream = IceCream()
        ice_cream.add_flavor(MixIn("Chocolate", 3.00))
        self.assertEqual(len(ice_cream.get_flavors()), 1)

    def test_get_total(self):
        ice_cream = IceCream()
        ice_cream.add_flavor(MixIn("Chocolate", 3.00))
        ice_cream.add_flavor(MixIn("Vanilla", 3.00))
        self.assertEqual(ice_cream.get_total(), 6.00)

if __name__ == '__main__':
    unittest.main()

# tests/test_order.py
import unittest
from api.ice_cream import IceCream
from api.order import Order

class TestOrder(unittest.TestCase):
    def test_add_item(self):
        order = Order()
        ice_cream = IceCream()
        order.add_item(ice_cream)
        self.assertEqual(len(order.items), 1)

    def test_get_total(self):
        order = Order()
        ice_cream = IceCream()
        ice_cream.add_flavor(MixIn("Chocolate", 3.00))
        ice_cream.add_flavor(MixIn("Vanilla", 3.00))
        order.add_item(ice_cream)
        self.assertEqual(order.get_total(), 6.00)

if __name__ == '__main__':
    unittest.main()
