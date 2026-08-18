import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL  # Импортируем URL из файла с данными


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    @allure.step('Ожидание и поиск элемента')
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Клик по элементу')
    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Ввод текста в поле')
    def input_text(self, locator, text, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        element.send_keys(text)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Получение текста элемента')
    def get_text(self, locator, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        return element.text
