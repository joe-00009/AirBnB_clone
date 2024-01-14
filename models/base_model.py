#!/usr/bin/python3
"""Defines the BaseModel Class."""
import models
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """

        """
        kk = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, kk)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        rerutn f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
