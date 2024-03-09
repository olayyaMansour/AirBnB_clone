#!/usr/bin/python3
"""Module for FileStorage class."""

import json

class FileStorage:
    """FileStorage class for AirBnB project."""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_dict = {}
        for key, value in self.__objects.items():
            serialized_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_dict = json.load(file)
            for key, value in loaded_dict.items():
                class_name, obj_id = key.split('.')
                self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
