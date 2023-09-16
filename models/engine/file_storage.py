#!/usr/bin/python3
"""FileStorage class that serializes and deserializes
   JSON file to instances."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents the FileStorage class.
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty dictionary but will
        store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        new_dict = FileStorage.__objects
        obj_dict = {obj: new_dict[obj].to_dict() for obj in new_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
