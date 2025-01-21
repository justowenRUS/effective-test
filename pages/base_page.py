from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        # Инициализация страницы
        self.page = page
    
    def navigate(self, url: str):
        """
        Переходит на указанный URL.
        
        Строка с адресом, куда нужно перейти.
        """
        # Переходим по указанному URL
        self.page.goto(url)
    
    def get_url(self):
        """
        Возвращает текущий URL страницы.
        
        Текущий URL страницы.
        """
        # Получаем текущий URL страницы
        return self.page.url