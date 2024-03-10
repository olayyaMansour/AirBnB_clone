#!/usr/bin/python3
"""
Test for creating BaseModel from dictionary
"""

import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    def test_create_from_dict(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()

        new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
