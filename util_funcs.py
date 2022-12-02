import random
import string
import sys
import os
import typing

""" This module is all about the lock content - it is used to encrypt a plaintext message.
For example, it generates lock files, creates unique names,
writes lock values, and checks/validates the lock depth. """
def generate_lock_file(size):
    """ this function creates lock files used to encrypt a text and gives error msg if it cannot"""
    # generate random lock file name: [random]_lock.txt
    lock_file_name = generate_unique_lock_file_name()
    try:
        return write_to_lock_file(lock_file_name, size)
    except Exception as file_error:
        print(f'\n\tAn error occurred while trying to write to {lock_file_name}:{file_error}\n')
        return None

def generate_unique_lock_file_name():
    """ this function creates unique names every time a lock file is created """
    files_in_dir = os.listdir()
    for i in range(30):
        random_file_name = '_lock.txt'
        for _ in range(8):
            random_letter = random.choice(string.ascii_letters)
            random_file_name = random_letter + random_file_name
        if random_file_name not in files_in_dir:
            break
    return random_file_name

def write_lock_values_to_file(num_values: int, file_obj: typing.TextIO):
    """ this function writes the lock Values of the encrypted text to a file """
    for line_ct in range(int(num_values)):
        rand_int1 = random.randint(0, sys.maxsize)
        if line_ct < int(num_values) - 1:
            print(f'{rand_int1}', file=file_obj)
            continue
        file_obj.write(f'{rand_int1}')

def write_to_lock_file(file_name, size_val):
    """ this function writes to a (lock) text file """
    with open(file_name, 'w') as text_file:
       write_lock_values_to_file(size_val, text_file)
       return file_name

def lock_depth_positive_check(depth, arg_val):
   """ this function checks if the locks depth is less than or equal to 0  """
   if depth <= 0:
       print(f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n')
       return None
   return depth

def validate_lock_depth(arg_value: str):
   """ this function thoroughly checks if the locks depth is a positive integer """
   try:
       lock_depth = int(arg_value)
       return lock_depth_positive_check(lock_depth, arg_value)
   except ValueError:
       print(f'\n\tInvalid lock depth: \'{arg_value}\'. Must be an integer greater than 0 (zero).\n')
   return None
