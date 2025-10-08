# tests/test_app.py
from app.main import greet_user  # or adjust path if it's in utils.py

def test_greet_user():
    assert greet_user("Ananya") == "Hello, Ananya!"
