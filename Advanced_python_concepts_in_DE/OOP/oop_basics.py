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

