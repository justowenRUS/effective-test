# **Playwright + Pytest + Allure**

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![Pytest](https://img.shields.io/badge/Pytest-%3E%3D8.0-orange.svg)  
![Static Badge](https://img.shields.io/badge/Allure-%3E%3D2.13-darkyellow.svg)

---

## **Установка и настройка**

### **1. Установка зависимостей**

```sh
git clone https://github.com/justowenRUS/effective-test
cd effective-test
pip install -r requirements.txt
```

### **2. Установка Playwright**

```sh
playwright install
```

---

## **Запуск тестов**

### **Запуск тестов с отчетом `Allure`**

```sh
pytest --alluredir results
allure generate .\results\
allure serve reports
```

---

## **Структура проекта**

```
effective-test/
│── tests/
│   ├── test_main_page.py
│
│── pages/
│   ├── base_page.py
│   ├── main_page.py
│
│── conftest.py
│── requirements.txt
│── README.md
```

---

## **Пример теста**

```python
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
```
