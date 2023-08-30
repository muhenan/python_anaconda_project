from typing import Optional

from pydantic import BaseModel, ValidationError
import unittest

print("Pydantic Test")


class Person(BaseModel):
    p_id: int
    first_name: str
    last_name: str
    age: int
    spouse: Optional[str] = None

"""
The behavior you're observing is due to the way Python's context managers work, including how
exceptions are raised and captured. Let's break down what's happening step by step:

When you use the with statement along with assertRaises, you're essentially telling Python to
enter a context where you expect a certain exception to be raised.

Inside the context (within the indented block of code), any code that would raise the specified
exception is captured by the context manager, and the exception is not propagated further.

After the block, the context manager checks whether the expected exception was indeed raised.
If it was, the test passes. If it wasn't, the test fails.

"""

class PydanticTest(unittest.TestCase):
    def test_pydantic(self):
        with self.assertRaises(ValidationError) as cm:  # cm context manager
            Person(p_id=23, first_name="Mike")

        print(type(cm))
        ers = cm.exception.errors()
        print(type(ers))
        print(type(cm.exception))
        my_exception = cm.exception
        actual = str(cm.exception)
        print(my_exception)

        assert "Field required" in actual
        assert "age\n" in actual
        assert "p_id\n" not in actual

        print("HHHH")


unittest.main()
