import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL


@allure.feature("Заказ самоката и переходы")
class TestScooterOrderAndLogos:

    # Два набора тестовых данных
    ORDER_DATA = [
        ("Иван", "Иванов", "Москва, ул. Ленина, 1", "Черкизовская", "+79991112233", "20.06.2026", "Позвонить за час", "black"),
        ("Пётр", "Петров", "Москва, Тверская, 15", "Охотный Ряд", "+79992223344", "21.06.2026", "Оставить у двери", "grey")
    ]

    @pytest.mark.parametrize(
        "click_order_button",
        [
            MainPage.click_top_order_button,
            MainPage.click_bottom_order_button
        ],
        ids=["top_button", "bottom_button"]
    )
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, comment, color", ORDER_DATA)
    @allure.title("Позитивный сценарий заказа самоката")
    def test_positive_order_flow(self, driver, click_order_button, name, surname, address, metro, phone, date, comment, color):
        main_page = MainPage(driver)
        main_page.accept_cookies_if_needed()

        # Вызываем метод напрямую без условных операторов
        click_order_button(main_page)

        order_page = OrderPage(driver)
        # Заполняем первую часть формы
        order_page.fill_personal_info(name, surname, address, metro, phone)
        # Заполняем вторую часть формы
        order_page.fill_rent_info(date, comment, color)
        # Подтверждаем заказ
        order_page.confirm_order()

        # Проверяем успешность создания заказа
        assert order_page.is_success_modal_displayed(), "Модальное окно успешного заказа не появилось!"

    @allure.title("Проверка редиректа на главную страницу Самоката при клике на логотип")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies_if_needed()
        main_page.click_top_order_button()   # Переходим на страницу заказа, чтобы было откуда возвращаться
        
        main_page.click_scooter_logo()
        assert BASE_URL in driver.current_url

    @allure.title("Проверка редиректа на Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies_if_needed()
        
        main_page.click_yandex_logo()
        
        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])
        
        # Проверяем, что новая вкладка открылась
        assert len(driver.window_handles) > 1, "Новая вкладка с Дзеном не открылась!"
