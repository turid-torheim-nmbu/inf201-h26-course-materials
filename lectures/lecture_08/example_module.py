"""
Module: example_module
Description: Template for a PEP 8 compliant Python class.
Author: Your Name (this template was created by Gemini)
Date: YYYY-MM-DD
"""

from typing import Any


class ClassName:
    """A brief description of what this class does."""

    def __init__(self, param1: Any, param2: Any) -> None:
        """
        Initialize the ClassName instance.

        Args:
            param1 (Any): Description of the first parameter.
            param2 (Any): Description of the second parameter.

        Raises:
            ValueError: If parameters are invalid.
        """
        # Input validation
        if param1 is None or param2 is None:
            raise ValueError("param1 and param2 cannot be None.")

        self.param1 = param1
        self.param2 = param2

    def method_name(self, arg1: Any) -> Any:
        """
        Perform an operation.

        Args:
            arg1 (Any): Description of the argument.

        Returns:
            Any: Description of the return value.
        """
        # Example logic
        return f"Processed {arg1} with {self.param1} and {self.param2}"

    @staticmethod
    def utility_method(arg: Any) -> bool:
        """
        A static utility method.

        Args:
            arg (Any): Description of the argument.

        Returns:
            bool: True if condition met, otherwise False.
        """
        return arg is not None

    @classmethod
    def create_default(cls) -> ClassName:
        """
        Create a default instance of ClassName.

        Returns:
            ClassName: A default instance.
        """
        return cls(param1="default1", param2="default2")


if __name__ == "__main__":
    # Example usage
    try:
        obj = ClassName(param1="Hello", param2="World")
        print(obj.method_name("Test"))
        print(ClassName.utility_method("Check"))
        default_obj = ClassName.create_default()
        print(default_obj.method_name("Default Test"))
    except ValueError as err:
        print(f"Error: {err}")
