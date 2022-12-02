import pytest
import util_funcs
from print_functions import *
from testfixtures import TempDirectory
from util_funcs import lock_depth_positive_check

""" 
This is the automated unit test module for this project. 
Every function begins with test_, so python/pytest knows its used for testing
"""

def test_print_separation_line(capfd):
    """ this function tests the separation line function in print_functions.py """
    print_separation_line('=', 2)
    out, err = capfd.readouterr()
    assert out == '\n\t==\n\n'

    print_separation_line('=', 0)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'

    print_separation_line('=', 10)
    out, err = capfd.readouterr()
    assert out == '\n\t==========\n\n'

    print_separation_line('', 2)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'

    print_separation_line('=', -1)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'

    with pytest.raises(TypeError) as error:
        print_separation_line(None, 2)
    assert error.type is TypeError


def test_extract_msg_file_content(capfd):
    """ this function tests the extract message content in print_functions.py and
    creates a temporary text file and deletes after the test is done """
    with TempDirectory() as tempDir:
        temp_filename = 'test.txt'
        test_line = b'Testing...'
        tempDir.write(temp_filename, test_line)
        file_path = tempDir.path + '\\' + temp_filename
        extract_msg_file_content(file_path)
    out, err = capfd.readouterr()
    assert out == 'Testing...\n'
    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as file_error:
        extract_msg_file_content(missing_file)
    assert file_error.type is FileNotFoundError


def test_lock_depth_positive_check(capfd):
    """ this function tests if the lock depth is a positive integer """
    util_funcs.lock_depth_positive_check(20, '20')
    out, err = capfd.readouterr()
    assert out != 20

    lock_depth, arg_val = 0, '0'
    assert lock_depth_positive_check(lock_depth, arg_val) is None
    stdout, err = capfd.readouterr()
    assert stdout == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n\n'

    lock_depth, arg_val = -1, '-1'
    assert lock_depth_positive_check(lock_depth,arg_val) is None
    stdout, err = capfd.readouterr()
    assert stdout == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n\n'

