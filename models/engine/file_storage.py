from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class CustomFileStorage:
	"""Defines a custom storage engine for managing object serialization.

	Attributes:
		__file_path (str): The name of the file used to store objects.
		__objects (dict): A dictionary to hold objects.
	"""
	__file_path = "custom_file.json"
	__objects = {}

	def all(self):
		"""Returns the dictionary of stored objects (__objects)."""
		return CustomFileStorage.__objects

	def new(self, obj):
		"""Adds a new object to __objects with the key <obj_class_name>.id."""
		class_name = obj.__class__.__name__
		CustomFileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

	def save(self):
		"""Serializes __objects to the JSON file specified by __file_path."""
		obj_dict = CustomFileStorage.__objects
		serialized_dict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
		with open(CustomFileStorage.__file_path, "w") as file:
			json.dump(serialized_dict, file)

	def reload(self):
		"""Deserializes the JSON file specified by __file_path to __objects, if it exists."""
		try:
			with open(CustomFileStorage.__file_path) as file:
				obj_dict = json.load(file)
				for obj_data in obj_dict.values():
					class_name = obj_data["__class__"]
					del obj_data["__class__"]
					self.new(eval(class_name)(**obj_data))
		except FileNotFoundError:
			return
