#!/usr/bin/python3
"""Unittest for the Square class.
"""
import unittest
import io
import os
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

    def test_square_1(self):
        """Square(1) sets width, height to 1, x/y default to 0."""
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_square_1_2(self):
        """Square(1, 2) sets size and x."""
        s = Square(1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 0))

    def test_square_1_2_3(self):
        """Square(1, 2, 3) sets size, x and y."""
        s = Square(1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 2, 3))

    def test_square_1_2_3_4(self):
        """Square(1, 2, 3, 4) also sets the id."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

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

    def test_square_str_1(self):
        """Square("1") raises a TypeError for width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_1_str_2(self):
        """Square(1, "2") raises a TypeError for x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_1_2_str_3(self):
        """Square(1, 2, "3") raises a TypeError for y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_neg1(self):
        """Square(-1) raises a ValueError for width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_1_neg2(self):
        """Square(1, -2) raises a ValueError for x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_1_2_neg3(self):
        """Square(1, 2, -3) raises a ValueError for y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_0(self):
        """Square(0) raises a ValueError for width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestSquareStr(unittest.TestCase):
    """Test cases for Square.__str__."""

    def test_str(self):
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

    def test_display(self):
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

    def test_update_no_args(self):
        """update() with no arguments changes nothing."""
        s = Square(5)
        before = str(s)
        s.update()
        self.assertEqual(str(s), before)

    def test_update_89(self):
        """update(89) updates only the id."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """update(89, 1) updates id and size."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_89_1_2(self):
        """update(89, 1, 2) updates id, size and x."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_89_1_2_3(self):
        """update(89, 1, 2, 3) updates id, size, x and y."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test cases for Square.update with **kwargs."""

    def test_update_kwargs_id(self):
        """update(**{'id': 89}) updates only the id."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """update(**{'id': 89, 'size': 1}) updates id and size."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        """update(**{...}) updates id, size and x."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_id_size_x_y(self):
        """update(**{...}) updates id, size, x and y."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_args_take_priority_over_kwargs(self):
        """If args is non-empty, kwargs is ignored entirely."""
        s = Square(5)
        s.update(1, size=99)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)


class TestSquareToDictionary(unittest.TestCase):
    """Test cases for Square.to_dictionary."""

    def test_to_dictionary(self):
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


class TestSquareCreate(unittest.TestCase):
    """Test cases for Square.create."""

    def test_create_kwargs_id(self):
        """Square.create(**{'id': 89}) creates an instance with id=89."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_kwargs_id_size(self):
        """Square.create(**{...}) sets id and size."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_kwargs_id_size_x(self):
        """Square.create(**{...}) sets id, size and x."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_kwargs_id_size_x_y(self):
        """Square.create(**{...}) sets id, size, x and y."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")


class TestSquareSaveToFile(unittest.TestCase):
    """Test cases for Square.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_none(self):
        """Square.save_to_file(None) writes an empty JSON list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Square.save_to_file([]) writes an empty JSON list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_square(self):
        """Square.save_to_file([Square(1)]) writes its dictionary."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))


class TestSquareLoadFromFile(unittest.TestCase):
    """Test cases for Square.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """load_from_file() when the file doesn't exist returns []."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing_file(self):
        """load_from_file() when the file exists returns instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        for obj in loaded:
            self.assertIsInstance(obj, Square)


if __name__ == "__main__":
    unittest.main()
