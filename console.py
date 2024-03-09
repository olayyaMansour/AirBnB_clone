#!/usr/bin/python3
"""Command Interpreter for AirBnB project."""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Command Interpreter class."""
    
    prompt = "(hbnb) "
    file_path = "file.json"
    storage = FileStorage()
    storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program at end of file (EOF)."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
