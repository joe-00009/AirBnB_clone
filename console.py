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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
