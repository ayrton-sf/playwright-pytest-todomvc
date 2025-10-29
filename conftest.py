import pytest
from pom_todo import HomePage

@pytest.fixture
def home(page):
    return HomePage(page)