from .base_page import BasePage

class MainPage(BasePage):
    ABOUT_US_LINK = '//*[@id="rec573054532"]/div/div/div[6]/a'
    SERVICES_LINK = '//*[@id="rec573054532"]/div/div/div[7]/a'
    PROJECTS_LINK = '//*[@id="rec573054532"]/div/div/div[8]/a'
    REVIEWS_LINK = '//*[@id="rec573054532"]/div/div/div[11]/a'
    CONTACTS_LINK = '//*[@id="rec573054532"]/div/div/div[9]/a'
    SPECIALISTS_LINK = '//*[@id="rec573054532"]/div/div/div[10]/a'
    LOGO_LINK = '//*[@id="rec573054532"]/div/div/div[4]/div/a'

    def click_about_us_link(self):
        self.page.wait_for_selector(self.ABOUT_US_LINK, state='visible')
        self.page.click(self.ABOUT_US_LINK)

    def click_services_link(self):
        self.page.wait_for_selector(self.SERVICES_LINK, state='visible')
        self.page.click(self.SERVICES_LINK)

    def click_projects_link(self):
        self.page.wait_for_selector(self.PROJECTS_LINK, state='visible')
        self.page.click(self.PROJECTS_LINK)

    def click_reviews_link(self):
        self.page.wait_for_selector(self.REVIEWS_LINK, state='visible')
        self.page.click(self.REVIEWS_LINK)

    def click_contacts_link(self):
        self.page.wait_for_selector(self.CONTACTS_LINK, state='visible')
        self.page.click(self.CONTACTS_LINK)

    def click_specialists_link(self):
        self.page.wait_for_selector(self.SPECIALISTS_LINK, state='visible')
        self.page.click(self.SPECIALISTS_LINK)

    def click_logo_link(self):
        self.page.wait_for_selector(self.LOGO_LINK, state='visible')
        self.page.click(self.LOGO_LINK)
