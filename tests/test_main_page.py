import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage

@pytest.mark.parametrize("link_selector, expected_url", [
    (MainPage.ABOUT_US_LINK, "#about"),
    (MainPage.SERVICES_LINK, "#moreinfo"),
    (MainPage.PROJECTS_LINK, "#cases"),
    (MainPage.REVIEWS_LINK, "#Reviews"),
    (MainPage.CONTACTS_LINK, "#contacts"),
    (MainPage.SPECIALISTS_LINK, "#specialists"),
    (MainPage.LOGO_LINK, "#main")
])
def test_navigation(page: Page, link_selector: str, expected_url: str):
    """
    Проверяет навигацию по различным ссылкам на сайте.
    
    page: Объект страницы Playwright.
    link_selector: Локатор для ссылки, которую нужно кликнуть.
    expected_url: Ожидаемый фрагмент URL после перехода.
    """
    # Создаем экземпляр главной страницы
    main_page = MainPage(page)
    
    # Переходим на начальную страницу
    main_page.navigate("https://effective-mobile.ru")
    
    # Ожидаем полной загрузки страницы
    page.wait_for_load_state('load')
    
    # Кликаем по выбранной ссылке
    page.click(link_selector)
    
    # Получаем текущий URL и проверяем, содержит ли он ожидаемый фрагмент
    current_url = main_page.get_url()
    assert expected_url in current_url, f"Неожиданный URL: {current_url}, ожидалось: {expected_url}"