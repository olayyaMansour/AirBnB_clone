#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """
    def test_init(self):
        """
        Test initialization of BaseModel instance
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str(self):
        """
        Test __str__ method of BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_output = "[BaseModel] ({}) {'my_number': 89, 'name': 'My First Model', "\
                          "'updated_at': datetime.datetime, 'id': '{}', "\
                          "'created_at': datetime.datetime}".format(my_model.id, my_model.id)
        self.assertEqual(str(my_model), expected_output)

    def test_save(self):
        """
        Test save method of BaseModel
        """
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
