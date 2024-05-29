from abc import ABC, abstractmethod
from pprint import pprint
import csv

class Cupcake(ABC):
    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling=None):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        pass

class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        super().__init__(name, price, flavor, frosting)

    def calculate_price(self, quantity):
        return quantity * self.price

class Large(Cupcake):
    size = "large"

    def calculate_price(self, quantity):
        return quantity * self.price


# Cupcake instances
cupcake1 = Mini("Widdle Wadder", 2.99, "Vanilla", "Vanilla")
cupcake1.add_sprinkles("Green")
cupcake2 = Mini("Uma Thurman", 1.99, "Chocolate", "Chocolate")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Regular("Spongey boy", 3.99, "Sponge Cake", "Cream Cheese")
cupcake4 = Regular("OG Bogey", 2.99, "Chocolate", "Chocolate", "Chocolate")
cupcake1.add_sprinkles("Chocolate")
cupcake5 = Large("KumbaKarna", 8.99, "Strawberry", "Vanilla")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
]

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            "size": cupcake.size,
            "name": cupcake.name,
            "price": cupcake.price,
            "flavor": cupcake.flavor,
            "frosting": cupcake.frosting,
            "filling": cupcake.filling,
            "sprinkles": cupcake.sprinkles
        })

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cupcake in cupcakes:
            writer.writerow({
                "size": cupcake.size,
                "name": cupcake.name,
                "price": cupcake.price,
                "flavor": cupcake.flavor,
                "frosting": cupcake.frosting,
                "filling": cupcake.filling,
                "sprinkles": cupcake.sprinkles
            })

def get_cupcakes(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    try:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                pprint(row)
    except FileNotFoundError:
        print(f"File {file} not found.")
    except Exception as e:
        print(f"Error reading {file}: {e}")
