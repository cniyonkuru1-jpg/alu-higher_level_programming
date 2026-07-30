#!/usr/bin/python3
"""Unittest for the Square class.
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test cases for creating Square instances."""

    def test_is_rectangle_instance(self):
        """A Square is also an instance of Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_is_base_instance(self):
        """A Square is also an instance of Base."""
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_width_height_equal_size(self):
        """width and height are both set to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_x_y_assigned(self):
        """x and y are assigned from the constructor."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_id_assigned(self):
        """The id argument is forwarded correctly."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.id, 12)

    def test_no_new_attributes(self):
        """Square doesn't define any new instance attributes."""
        s = Square(5)
        rectangle_attrs = {
            "_Rectangle__width",
            "_Rectangle__height",
            "_Rectangle__x",
            "_Rectangle__y",
            "id",
        }
        self.assertEqual(set(s.__dict__.keys()), rectangle_attrs)


class TestSquareValidation(unittest.TestCase):
    """Test cases for Square attribute validation (inherited)."""

    def test_size_not_int_raises_type_error(self):
        """A non-integer size raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero_raises_value_error(self):
        """A size of 0 raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_negative_raises_value_error(self):
        """A negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_negative_raises_value_error(self):
        """A negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)


class TestSquareStr(unittest.TestCase):
    """Test cases for Square.__str__."""

    def test_str_format(self):
        """__str__ follows [Square] (id) x/y - size."""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_str_default_offsets(self):
        """__str__ reflects default x/y of 0."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquareArea(unittest.TestCase):
    """Test cases for Square.area (inherited from Rectangle)."""

    def test_area(self):
        """Area is size squared."""
        s = Square(4)
        self.assertEqual(s.area(), 16)


class TestSquareDisplay(unittest.TestCase):
    """Test cases for Square.display (inherited from Rectangle)."""

    def setUp(self):
        """Redirect stdout to capture printed output."""
        self.held_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.original_stdout

    def test_display_no_offset(self):
        """display() prints a size x size block of '#'."""
        s = Square(2)
        s.display()
        self.assertEqual(self.held_output.getvalue(), "##\n##\n")


class TestSquareSize(unittest.TestCase):
    """Test cases for the Square.size property."""

    def test_size_getter(self):
        """size getter returns the current width/height."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter_updates_width_and_height(self):
        """Setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validates_type(self):
        """size setter raises TypeError for non-integers."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_size_setter_validates_value(self):
        """size setter raises ValueError for size <= 0."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquareUpdateArgs(unittest.TestCase):
    """Test cases for Square.update with *args."""

    def test_update_id_only(self):
        """A single positional argument updates only the id."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_id_size(self):
        """Two positional arguments update id and size."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual((s.id, s.size), (1, 2))

    def test_update_all_positional(self):
        """Four positional arguments update every attribute."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test cases for Square.update with **kwargs."""

    def test_update_single_kwarg(self):
        """A single keyword argument updates that attribute."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)

    def test_update_multiple_kwargs(self):
        """Multiple keyword arguments update multiple attributes."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_args_take_priority_over_kwargs(self):
        """If args is non-empty, kwargs is ignored entirely."""
        s = Square(5)
        s.update(1, size=99)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)


class TestSquareToDictionary(unittest.TestCase):
    """Test cases for Square.to_dictionary."""

    def test_dictionary_keys_and_values(self):
        """to_dictionary returns the correct keys and values."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_dictionary_type(self):
        """to_dictionary returns a dict."""
        s = Square(1)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_round_trip_equality(self):
        """A Square updated from its own dictionary matches it."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
