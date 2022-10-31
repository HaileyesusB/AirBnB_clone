#!/usr/bin/python3
"""Console"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Cmd class"""
    intro = "This AirBnB console"
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit"""
        exit()
        
    def do_EOF(self, arg):
        """Exit"""
        return True
    
    def help_quit(self):
        """Help"""

        print("Quit the program")

    def help_EOF(self):
        """Help quit"""
        print("Close AirBnB (hbnb) Shell")

    def emptyline(self):
        """move to next line"""
        pass

    def help_emptyline(self):
        """Overriding the emptyline()"""
        print("Help emptyline")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id. Ex: $ create BaseModel
        """

        if arg == None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print(" ** class doesn't exist **")
        else:
            arg = BaseModel()
            arg.save()
            print("{}".format(arg["id"]))

    def do_show(self, mod, id):
        """Prints the string representation of an 
        instance based on the class name and id
        """

        if mod == None:
            print("** class name missing **")
        elif mod != 'BaseModel':
            print("** class doesn't exist **")
        elif id == None:
            print("** instance id missing **")
        elif id.strip() != BaseModel.get('id'):
            print("** no instance found **")
        else:
            str(mod)
        
    def do_destroy(self, mod, id):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """

        if mod == None:
            print("** class name missing **")
        elif mod != 'BaseModel':
            print("** class doesn't exist **")
        elif id == None:
            print("** instance id missing **")
        elif id.strip() != BaseModel.get('id'):
            print("** no instance found **")
        else:
            mod.save()
            mod = {}

    def all(self, mod):
        """Prints all string representation of all instances based or != on the class name.
         Ex: $ all BaseModel or $ all
        """

        if mod != 'BaseModel':
            print("** class doesn't exist **")      
        else:
            print("AM stack men")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
