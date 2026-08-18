from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    COOKIE_BTN = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BTN = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    BOTTOM_ORDER_BTN = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")

    # Шаблон для вопросов и ответов в аккордеоне («Вопросы о важном»)
    @staticmethod
    def get_question_locator(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def get_answer_locator(index):
        return By.ID, f"accordion__panel-{index}"

    def accept_cookies_if_needed(self):
        try:
            self.click_element(self.COOKIE_BTN, timeout=3)
        except:
            pass

    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BTN)

    def click_bottom_order_button(self):
        self.scroll_to_element(self.BOTTOM_ORDER_BTN)
        self.click_element(self.BOTTOM_ORDER_BTN)

    def click_scooter_logo(self):
        self.click_element(self.LOGO_SCOOTER)

    def click_yandex_logo(self):
        self.click_element(self.LOGO_YANDEX)

    def click_question(self, index):
        locator = self.get_question_locator(index)
        self.scroll_to_element(locator)
        self.click_element(locator)

    def get_answer_text(self, index):
        locator = self.get_answer_locator(index)
        return self.get_text(locator)