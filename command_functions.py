import json
import os
import print_functions
import util_funcs
from lock_functions import lock
from unlock_functions import unlock
from print_functions import print_separation_line

""" this module is all about the command functions to which the user can select a variety of commands to use,
 specifically to either to encrypt/decrypt, clear, help, or getting a list of encrypted/decrypted messages  """

def help_command():
    """this function displays the help command in which the user sees a list of ll commands and includes separation of lines """
    print_functions.print_separation_line('=', 50)
    print_functions.print_welcome_message()
    print_functions.print_separation_line('=', 50)
    print_functions.print_help_welcome()
    print_functions.print_separation_line('=', 50)
    print_functions.print_lock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_unlock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_msg_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_locked_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_clear_help()
    print_functions.print_separation_line('=', 50)

def msg_command():
    """this function prints a list of all decrypted messages and files they are stored in and otherwise  """
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
    if len(decrypted_file_list) == 0:
        print('\n\tNo plaintext message files available.\n')
    else:
        print('\n\tPlaintext message files:\n')
        for file_name in decrypted_file_list:
            print(f'\t{file_name}', end='')
            print_functions.extract_msg_file_content(file_name)
            print_functions.print_msg_file_info(file_name)

def locked_command():
    """ this functions prints a list of the encrypted messages and files they are stored in and prints otherwise if not"""
    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    if len(encrypted_file_list) == 0:
        print('\n\tNo encrypted message files available.\n')
    else:
        print('\n\tEncrypted message files:\n')
        for file_name in encrypted_file_list:
            print(f'\t{file_name}')
            print_functions.extract_locked_file_content(file_name)
            print_functions.print_locked_file_info(file_name)

def clear_command():
    """ this function deletes encrytped/decryped/etc. in the jlock project directory. 'It resets' """
    lock_file_list = [file for file in os.listdir() if file.endswith('_lock.txt')]
    key_file_list = [file for file in os.listdir() if file.endswith('_key.txt')]
    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
    master_text_file_list = lock_file_list + key_file_list + encrypted_file_list + decrypted_file_list
    for text_file in master_text_file_list:
        os.remove(text_file)
        print('\n\n\tAll \'lock\', \'key\', \'encrypted message\', and \'decrypted message\' text files removed.\n')
    else:
        print('Error: invalid command')


def unlock_command(arg_list: list):
    """ this function is used to decrypt an encrypted message and prints if its invalid """
    target_encrypted_file: str = arg_list[2]
    file_list = os.listdir()
    if (target_encrypted_file in file_list) and (len(target_encrypted_file) == 22) and \
            (target_encrypted_file[-18:] == '_encrypted_msg.txt'):
        unlock(target_encrypted_file)
    else:
        print(f'\n\t{target_encrypted_file} does not exist or is invalid\n')


def lock_command(arg_list: list):
    """ this function is used to encrypt a plaintext message """
    util_funcs.validate_lock_depth(arg_list[2])
    lock_file = util_funcs.generate_lock_file(arg_list[2])
    lock(arg_list[3], lock_file)
