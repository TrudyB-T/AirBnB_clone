#!/usr/bin/python3
""" Class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
        Defines all common attributes/methods for other classes

        Attributes:
                   id: string - assigned with an uuid when
                                an instance is created
                   created_at: datetime of the instance created
                   updated_at: datetime is updated every
                               time you change your object
    """
    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
            Returns a string representation of the class BaseModel
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Returns a string representation of class BaseModel
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
             returns a dictionary containing all keys/values
             of __dict__ of the instance
        """
        cpy_d = dict(self.__dict__)
        cpy_d['__class__'] = self.__class__.__name__
        cpy_d['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cpy_d['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cpy_d)
