import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    # Инициализация Firefox через WebDriver Manager (либо стандартный запуск)
    options = webdriver.FirefoxOptions()
    # options.add_argument("--headless") # Раскомментируй, если тесты нужно запускать без графического интерфейса
    
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    yield driver
    
    driver.quit()