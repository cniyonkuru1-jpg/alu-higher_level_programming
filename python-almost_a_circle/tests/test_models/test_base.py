#!/usr/bin/python3
"""Unittest for the Base class.
"""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class instantiation and id logic."""

    def test_id_assigned(self):
        """A given id is assigned as-is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_is_public(self):
        """The id attribute is accessible publicly."""
        b = Base(5)
        self.assertTrue(hasattr(b, "id"))

    def test_base_no_args_assigns_id_automatically(self):
        """Base() assigns an id automatically."""
        b = Base()
        self.assertIsNotNone(b.id)

    def test_base_auto_id_increments(self):
        """Base() assigns id = previous auto id + 1."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_89_saves_id_passed(self):
        """Base(89) saves the id passed as argument."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_zero(self):
        """An id of 0 is respected, not treated as falsy/None."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """A negative id is accepted as-is."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_no_args_no_id_kwarg(self):
        """Base() with no arguments works and assigns an id."""
        b = Base()
        self.assertIsNotNone(b.id)


class TestBaseToJSONString(unittest.TestCase):
    """Test cases for Base.to_json_string."""

    def test_to_json_string_none(self):
        """Base.to_json_string(None) returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Base.to_json_string([]) returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list_with_dict(self):
        """Base.to_json_string([{'id': 12}]) returns valid JSON."""
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(json.loads(result), [{'id': 12}])

    def test_to_json_string_returns_string(self):
        """Base.to_json_string([{'id': 12}]) returns a string."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_return_type_is_str(self):
        """The return value is always a string."""
        self.assertIsInstance(Base.to_json_string([{"a": 1}]), str)


class TestBaseFromJSONString(unittest.TestCase):
    """Test cases for Base.from_json_string."""

    def test_from_json_string_none(self):
        """Base.from_json_string(None) returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list_string(self):
        """Base.from_json_string("[]") returns an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list_with_dict(self):
        """Base.from_json_string('[{ "id": 89 }]') parses correctly."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Base.from_json_string('[{ "id": 89 }]') returns a list."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)

    def test_round_trip(self):
        """A list survives a to_json_string / from_json_string round trip."""
        list_dicts = [{"id": 1, "width": 10, "height": 4}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)


class TestBaseSaveToFile(unittest.TestCase):
    """Test cases for Base.save_to_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_creates_file(self):
        """save_to_file creates a file named <Class>.json."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_none_creates_empty_list_file(self):
        """save_to_file(None) writes an empty JSON list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites_existing_file(self):
        """save_to_file overwrites the file if it already exists."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 3)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["width"], 2)

    def test_save_content_matches_dictionaries(self):
        """The saved file content matches the objects' dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(content, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_square_uses_square_filename(self):
        """Square.save_to_file writes to Square.json."""
        s = Square(5)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))
        self.assertFalse(os.path.exists("Rectangle.json"))


class TestBaseCreate(unittest.TestCase):
    """Test cases for Base.create."""

    def test_create_rectangle(self):
        """Rectangle.create builds a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_create_returns_new_instance(self):
        """create returns a distinct object, not the original."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Square.create builds a Square from a dictionary."""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))


class TestBaseLoadFromFile(unittest.TestCase):
    """Test cases for Base.load_from_file."""

    def tearDown(self):
        """Remove any JSON files created during the tests."""
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_no_file_returns_empty_list(self):
        """load_from_file returns [] if the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_returns_list_of_instances(self):
        """load_from_file returns a list of the correct instance type."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        for obj in loaded:
            self.assertIsInstance(obj, Rectangle)

    def test_load_round_trip_matches_originals(self):
        """Loaded instances match the originals' dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(
            [o.to_dictionary() for o in loaded],
            [r1.to_dictionary(), r2.to_dictionary()],
        )

    def test_load_square_round_trip(self):
        """Loaded Square instances match the originals."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        for obj in loaded:
            self.assertIsInstance(obj, Square)


if __name__ == "__main__":
    unittest.main()
