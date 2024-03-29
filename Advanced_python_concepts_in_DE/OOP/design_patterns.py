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
        
    @abstractmethod
    def create_pizza(self, pizza_type):
        """
        Abstract method to create a pizza.

        Parameters:
        - pizza_type (str): Type of pizza to create.

        Returns:
        - Pizza: An instance of the created pizza.
        """
        pass

    def order_pizza(self, pizza_type):
        """
        Method to order a pizza.

        Parameters:
        - pizza_type (str): Type of pizza to order.

        Returns:
        - Pizza: An instance of the ordered pizza.
        """
        pizza = self.create_pizza(pizza_type)
        print(f"{self.name} is preparing to make {pizza.name} pizza.")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        print(f"{self.name} completed the order for {pizza.name} pizza.")
        return pizza

# ----------------------------------------------
# Concrete Creator Class: NYStylePizzaStore
# ----------------------------------------------

class NYStylePizzaStore(PizzaStore):
    """
    Concrete Creator: New York Style Pizza Store.
    """
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza("NY Style Margherita")
        elif pizza_type == "Pepperoni":
            return PepperoniPizza("NY Style Pepperoni")
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")

# ----------------------------------------------
# Main Program
# ----------------------------------------------

# Create an instance of the NYStylePizzaStore
ny_pizza_store = NYStylePizzaStore("NY Pizza Store")

# Order Margherita pizza
margherita_pizza = ny_pizza_store.order_pizza("Margherita")

# Order Pepperoni pizza
pepperoni_pizza = ny_pizza_store.order_pizza("Pepperoni")