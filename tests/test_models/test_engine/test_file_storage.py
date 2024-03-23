import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Tear down for the test"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        """Test the new method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_reload(self):
        """Test saving and reloading"""
        base_model = BaseModel()
        base_model.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)


if __name__ == "__main__":
    unittest.main()
