import sys
import command_functions
import print_functions
import util_funcs
import os
import json
from lock_functions import lock
from unlock_functions import unlock
from print_functions import print_separation_line

""" this module includes 2 functions only -  main and the command line parsing """

def jlock_main():
    """ this function gets the command line arguments and checks for empty string in command
    line args """
    arg_list = sys.argv
    if '' in arg_list:
        print('Error: invalid command')
        return
    parse_command_line_args(arg_list)

def parse_command_line_args(arg_list: list):
    """ this function checks the number of the command line arguments and what
    the second command line argument is and then the appropriate function is called """
    if len(arg_list) == 1:
        print_functions.print_welcome_message()
    elif len(arg_list) == 2:
        if arg_list[1] == '-help' or arg_list[1] == '-h':
            command_functions.help_command()
        if arg_list[1] == '-msg':
            command_functions.msg_command()
        if arg_list[1] == '-locked':
            command_functions.locked_command()
        if arg_list[1] == '-clear':
            command_functions.clear_command()
        else:
            print('Error: invalid command')
    elif len(arg_list) == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command(arg_list)
    elif len(arg_list) == 4:
        if arg_list[1] == '-lock':
            command_functions.lock_command(arg_list)
        else:
            print('Error: invalid command')
    else:
        print('Error : Invalid command')


if __name__ == '__main__':
    jlock_main()
