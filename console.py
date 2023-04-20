#!/usr/bin/python3
"""Defines hbnb command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """AirBnB command Interpreter"""

    prompt= "(hbnb)"
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Signal to exit the program"""
        return True
    
    def emptyline(self):
        """Execute nothing upon receiving empty line + Enter"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
