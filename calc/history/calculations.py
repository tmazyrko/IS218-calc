"""Calculation history class"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculations: # pylint: disable=too-few-public-methods
    """Calculations class managing the history of calculations"""

    history = []

    @staticmethod
    def clear_history():
        """Clears calculation history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Gets number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Gets most recent calculation in history"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result():
        """Gets value of the result of most recent calculation in history"""
        return Calculations.get_last_calculation_object().get_result()

    @staticmethod
    def get_first_calculation_object():
        """Gets first calculation in history"""
        return Calculations.history[0]

    @staticmethod
    def get_first_calculation_result():
        """Gets value of the result of first calculation in history"""
        return Calculations.get_first_calculation_object().get_result()

    @staticmethod
    def get_calculation(index):
        """Gets a specific calculation from history"""
        return Calculations.history[index]

    @staticmethod
    def add_calculation(calculation):
        """Add a generic calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_calculation_addition(values):
        """Create an Addition using factory method create and add object to history"""
        return Calculations.history.append(Addition.create(values))

    @staticmethod
    def add_calculation_subtraction(values):
        """Create a Subtraction using factory method create and add object to history"""
        return Calculations.history.append(Subtraction.create(values))

    @staticmethod
    def add_calculation_multiplication(values):
        """Create a Multiplication using factory method create and add object to history"""
        return Calculations.history.append(Multiplication.create(values))

    @staticmethod
    def add_calculation_division(values):
        """Create a Division using factory method create and add object to history"""
        return Calculations.history.append(Division.create(values))
