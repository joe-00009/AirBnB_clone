#!/usr/bin/python3
"""Module for the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the HBNBCommand class."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line handler."""
        pass

    def do_create(self, args):
        """ Creates a new instance, saves it, and prints the id """
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args)
            instance = cls()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, args):
        """ Prints all string representations of all instances """
        objects = storage.all()
        obj_list = []
        if not args:
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
        else:
            try:
                cls = eval(args)
            except NameError:
                print("** class doesn't exist **")
                return
            for key, obj in objects.items():
                if key.split(".")[0] == args:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        setattr(obj, args_list[2], args_list[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
