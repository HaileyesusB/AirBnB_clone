#!/usr/bin/python3
""" this Module contains the entry point of the command interpreter """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ the class HBNBCommand """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """ to exit the comand line"""
        return True

    def do_quit(self, args):
        """ to quit the promt"""
        return True

    def emptyline(self):
        """ if no argument given """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
