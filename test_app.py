
from main import add_numbers, greet

def test_add_numbers():
    assert add_numbers(10, 20) == 30

def test_greet():
    assert greet("Naveen") == "Hello, Naveen! Welcome to DevOps."
