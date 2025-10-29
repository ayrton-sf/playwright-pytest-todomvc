import pytest
from pom_todo import HomePage
from playwright.sync_api import expect
from config import config

@pytest.mark.smoke
def test_home_loads_and_has_header(home: HomePage):
    home.goto()
    assert home.header().text_content() == "todos"
    assert home.todo_container().is_visible()
    expect(home.footer()).to_contain_text("Double-click to edit a todo")
    expect(home.footer()).to_contain_text("Created by the TodoMVC Team")
    expect(home.footer()).to_contain_text("Part of TodoMVC")
    assert home.mvc_repo_hyperlink().get_attribute("href") == config.mvc_repo_url
    