from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    # Локаторы формы заказа (Первая страница: Для кого самокат)
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")

    # Локаторы формы заказа (Вторая страница: Про аренду)
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION_1DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_OPTION_2DAYS = (By.XPATH, "//div[text()='двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BTN = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']")
    
    # Модальное окно подтверждения
    CONFIRM_YES_BTN = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[text()='Заказ оформлен']")

    def fill_personal_info(self, name, surname, address, metro, phone):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.SURNAME_INPUT, surname)
        self.input_text(self.ADDRESS_INPUT, address)
        
        # Выбор станции метро
        self.click_element(self.METRO_INPUT)
        self.input_text(self.METRO_INPUT, metro)
        self.click_element((By.XPATH, f"//div[text()='{metro}']"))
        
        self.input_text(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BTN)

    def fill_rent_info(self, date, comment, color="black"):
        self.input_text(self.DATE_INPUT, date)
        self.driver.find_element(*self.DATE_INPUT).send_keys(Keys.ENTER)
        
        # Срок аренды
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        self.click_element(self.RENTAL_PERIOD_OPTION_1DAY)
        
        # Цвет
        if color == "black":
            self.click_element(self.COLOR_BLACK)
        else:
            self.click_element(self.COLOR_GREY)
            
        self.input_text(self.COMMENT_INPUT, comment)
        self.click_element(self.FINAL_ORDER_BTN)

    def confirm_order(self):
        self.click_element(self.CONFIRM_YES_BTN)

    def is_success_modal_displayed(self):
        return self.find_element_with_wait(self.SUCCESS_MODAL).is_displayed()