#!/usr/bin/python3
"""
Airbnb Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program\n")

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
if __name__ == '__main__':
    HBNBCommand().cmdloop()
