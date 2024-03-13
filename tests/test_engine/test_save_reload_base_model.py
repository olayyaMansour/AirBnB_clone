#!/usr/bin/python3
"""Test for BaseModel"""

import unittest
import json
from models import storage
from models.base_model import BaseModel


class TestBaseModelSaveReload(unittest.TestCase):
    """Test the saving and reloading of BaseModel instances"""

    def test_save_reload(self):
        """Test saving and reloading of BaseModel instances"""
        all_objs = storage.all()
        base_model_count = len(all_objs)

        # Create a new object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        base_model_count_after_save = len(all_objs)

        # Check if the object was properly saved
        self.assertEqual(base_model_count + 1, base_model_count_after_save)

        # Check if the object is in the JSON file
        with open(storage._FileStorage__file_path, 'r') as file:
            file_data = json.load(file)
            obj_key = "BaseModel." + my_model.id
            self.assertIn(obj_key, file_data)
            obj_data = file_data[obj_key]
            self.assertEqual(obj_data['name'], "My_First_Model")
            self.assertEqual(obj_data['my_number'], 89)

        # Test reloading the objects
        storage.reload()
        all_objs_after_reload = storage.all()
        base_model_count_after_reload = len(all_objs_after_reload)

        # Check if the number of objects is the same after reloading
        self.assertEqual(base_model_count_after_save,
                         base_model_count_after_reload)

        # Check if the reloaded object has the same attributes
        reloaded_model = all_objs_after_reload["BaseModel." + my_model.id]
        self.assertEqual(reloaded_model.name, "My_First_Model")
        self.assertEqual(reloaded_model.my_number, 89)


if __name__ == "__main__":
    unittest.main()
