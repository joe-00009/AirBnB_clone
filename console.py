#!/usr/bin/python3
"""
Airbnb Console
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")  # Print a newline for a better exit appearance
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF command"""
        print("Exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to the JSON file, and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg.split()[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_instance = eval(f"{class_name}()")
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[obj_key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            print([str(all_objs[obj]) for obj in all_objs if class_name in obj])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args or len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        obj_key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        if hasattr(all_objs[obj_key], attr_name):
            attr_type = type(getattr(all_objs[obj_key], attr_name))
            setattr(all_objs[obj_key], attr_name, attr_type(attr_value))
            storage.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

