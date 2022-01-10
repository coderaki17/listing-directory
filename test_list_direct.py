from _pytest.python_api import raises
from pytest import main
import list_direct
import pytest
from list_direct import return_list

def test_running():
    assert(return_list('/Users/akashrc/pytest'))

def test_output_is_list():
    assert(isinstance(return_list('/Users/akashrc/pytest'),list))

def test_content_check():
  if "list_direct.py" in return_list('/Users/akashrc/pytest'):
    assert(True)

if __name__ == "__main__":
    main()
    

    




