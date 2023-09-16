#!/usr/bin/python3
""" Initializes Python Package"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .place import Place
from .state import State
from .city import City
from .amenity import Amenity
from .review import Review

storage = FileStorage()
storage.reload()
