from abc import ABC, abstractmethod

# ----------------------------------------------
# FoodItem Base Class Definition
# ----------------------------------------------

class FoodItem(ABC):
    """
    FoodItem class: Represents a generic food item.

    Attributes:
    - name (str): The name of the food item.
    - calories (int): The calorie content of the food item.
    """
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    @abstractmethod
    def display_info(self):
        """
        Abstract method to display information about the food item.

        No parameters.
        Returns: None
        """
        pass

    def nutritional_info(self):
        """
        Method to display nutritional information about the food item.

        No parameters.
        Returns: None
        """
        print(f"{self.name} - Calories: {self.calories} kcal")
        
# ----------------------------------------------
# Dessert Class Definition (Inheritance)
# ----------------------------------------------

class Dessert(FoodItem):
    """
    Dessert class (inherits from FoodItem): Represents a dessert.

    Additional Attributes:
    - flavor (str): The flavor of the dessert.
    """
    def __init__(self, name, flavor, calories):
        """
        Constructor method (init) for Dessert class.

        Parameters:
        - name (str): The name of the dessert.
        - flavor (str): The flavor of the dessert.
        - calories (int): The initial calorie content of the dessert.
        """
        super().__init__(name, calories)
        self.flavor = flavor

# Overriding the display_info method from the base class
    def display_info(self):
        """
        Overridden method to display detailed information about the dessert.

        No parameters.
        Returns: None
        """
        print(f"Dessert: {self.name} - Flavor: {self.flavor}, Calories: {self.calories} kcal")

    # Additional method specific to desserts
    def enjoy(self, extra_calories=0):
        """
        Method to enjoy the dessert and add extra calories.

        Parameters:
        - extra_calories (int): Additional calories to add (default is 0).

        Returns: None
        """
        self.calories += extra_calories
        print(f"Enjoying {self.name}! Now it has {self.calories} calories.")

# ----------------------------------------------
# Main Program
# ----------------------------------------------

# Create instances of the Dessert class
dessert1 = Dessert("Chocolate Cake", "Chocolate", 300)
dessert2 = Dessert("Strawberry Ice Cream", "Strawberry", 150)

# Display detailed information about the desserts
dessert1.display_info()
dessert2.display_info()

# Enjoy the desserts, adding extra calories
dessert1.enjoy(50)
dessert2.enjoy(20)

# Display updated information after enjoying the desserts
dessert1.display_info()
dessert2.display_info()