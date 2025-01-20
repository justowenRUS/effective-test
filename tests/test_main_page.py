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
    main_page = MainPage(page)
    main_page.navigate("https://effective-mobile.ru")

    # Ожидание загрузки страницы
    page.wait_for_load_state('load')

    # Кликаем по ссылке
    page.click(link_selector)

    # Проверяем URL
    assert expected_url in main_page.get_url(), f"юрл {expected_url}"
