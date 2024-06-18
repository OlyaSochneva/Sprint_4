import pytest
from main import BooksCollector
@pytest.fixture(scope="function")
def setup():
    setup = BooksCollector()
    setup.add_new_book('Дюна')
    return setup