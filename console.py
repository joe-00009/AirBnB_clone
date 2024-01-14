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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        obj_list = []
        if not args:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split(".")[0] == args[0]:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                instance = storage.all()[key]
                setattr(instance, args[2], eval(args[3]))
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
