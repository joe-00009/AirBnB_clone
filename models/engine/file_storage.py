#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """Defines the FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**obj_data)
                    self.__objects[key] = obj
