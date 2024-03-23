#!/usr/bin/python3
"""
Console for the HBNB project
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Empty line should not execute anything
        """
        pass

    def precmd(self, line):
        """
        Check for empty line + spaces
        """
        if not line.strip():
            return "do_nothing"
        return line

    def do_nothing(self, line):
        """
        Does nothing when an empty line with spaces is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in BaseModel.__name__:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in BaseModel.__name__:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        objs = storage.all()
        if not arg:
            print([str(objs[key]) for key in objs])
            return
        elif arg not in BaseModel.__name__:
            print("** class doesn't exist **")
            return
        print([str(objs[key]) for key in objs if arg in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in BaseModel.__name__:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = args[0] + "." + args[1]
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
