from src.hello_world import hello_name
import pytest


def test_all():
    hello_name("bla")
    # pytest.fail("doesn't work")
