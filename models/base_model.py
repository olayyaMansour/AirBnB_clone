#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the BaseModel for all models in the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__create_from_kwargs(**kwargs)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return the dict representation of the instance."""
        raw_dict = self.__dict__.copy()
        raw_dict['created_at'] = self.created_at.isoformat()
        raw_dict['updated_at'] = self.updated_at.isoformat()
        raw_dict['__class__'] = type(self).__name__
        return raw_dict

    def __str__(self):
        """Return the string representation of the instance."""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def __create_from_kwargs(self, **kwargs):
        """Create an instance from dictionary kwargs"""
        for key, val in kwargs.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.fromisoformat(val)
                setattr(self, key, val)