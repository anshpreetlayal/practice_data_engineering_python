from abc import ABC, abstractmethod

# ----------------------------------------------
# Product Interface: Pizza
# ----------------------------------------------

class Pizza(ABC):
    """
    Pizza interface (Product): Represents a pizza.

    Attributes:
    - name (str): The name of the pizza.
    - toppings (list): List of toppings on the pizza.
    """
    def __init__(self, name):
        self.name = name
        self.toppings = []

    @abstractmethod
    def prepare(self):
        """
        Abstract method for preparing the pizza.

        No parameters.
        Returns: None
        """
        pass

    def bake(self):
        """
        Method to bake the pizza.

        No parameters.
        Returns: None
        """
        print(f"Baking {self.name} pizza.")

    def cut(self):
        """
        Method to cut the pizza.

        No parameters.
        Returns: None
        """
        print(f"Cutting {self.name} pizza.")

    def box(self):
        """
        Method to box the pizza.

        No parameters.
        Returns: None
        """
        print(f"Boxing {self.name} pizza.")


# ----------------------------------------------
# Concrete Product Classes: MargheritaPizza, PepperoniPizza
# ----------------------------------------------

class MargheritaPizza(Pizza):
    """
    Concrete Product: Margherita Pizza.
    """
    def prepare(self):
        print("Preparing Margherita pizza with tomato sauce and mozzarella.")

class PepperoniPizza(Pizza):
    """
    Concrete Product: Pepperoni Pizza.
    """
    def prepare(self):
        print("Preparing Pepperoni pizza with tomato sauce, mozzarella, and pepperoni.")

# ----------------------------------------------
# Creator Interface: PizzaStore
# ----------------------------------------------

class PizzaStore(ABC):
    """
    PizzaStore interface (Creator): Abstract class representing a pizza store.

    Methods:
    - order_pizza(type: str): Order a pizza of the specified type.

    Attributes:
    - name (str): The name of the pizza store.
    """
    def __init__(self, name):
        self.name = name