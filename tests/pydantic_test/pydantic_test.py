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
