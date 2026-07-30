#!/usr/bin/python3
"""Module that defines the Base class.

The Base class manages the id attribute for all future classes and
avoids duplicating the same code (and by extension, the same bugs).
"""
import json


class Base:
    """Base class that manages the id attribute of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance. If None, a
                unique id is generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: "[]" if list_dictionaries is None or empty, otherwise
            the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        The filename used is <Class name>.json, and it is overwritten
        if it already exists.

        Args:
            list_objs (list): A list of instances that inherit
                from Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): A string representing a list of
                dictionaries.

        Returns:
            list: An empty list if json_string is None or empty,
            otherwise the list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            dictionary (dict): Key/value pairs of attributes to
                initialize the new instance with.

        Returns:
            An instance of cls with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        The filename used is <Class name>.json.

        Returns:
            list: An empty list if the file doesn't exist, otherwise
            a list of instances of cls built from the file's content.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
