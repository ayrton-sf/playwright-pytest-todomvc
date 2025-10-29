from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("/")

    def header(self):
        return self.page.get_by_test_id("header").locator("h1")
    
    def todo_container(self):
        return self.page.locator(".input-container")

    def todo_input(self):
        return self.page.get_by_test_id("text-input")
    
    def footer(self):
        return self.page.locator("footer.info")
    
    def mvc_repo_hyperlink(self):
        return self.page.locator("footer.info").locator("a")
    
    def complete_all(self):
        return self.page.get_by_test_id("toggle-all")
    
    def todo_checkbox(self, todo_content: str):
        return self.page.locator("div", has_text=todo_content).get_by_test_id("todo-item-toggle")
    
    def todo_delete(self, todo_content: str):
        return self.page.locator("div", has_text=todo_content).get_by_test_id("todo-item-button")
    
    def clear_completed(self):
        return self.page.locator('.clear-completed')
    
    def filter_all(self):
        return self.page.locator('.filters').get_by_text("All")

    def filter_active(self):
        return self.page.locator('.filters').get_by_text("Active")
    
    def filter_completed(self):
        return self.page.locator('.filters').get_by_text("Completed")

    def todo_list_container(self):
        return self.page.get_by_test_id("todo-list")
