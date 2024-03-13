#!/usr/bin/python3
"""
Console for the HBNB project
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
