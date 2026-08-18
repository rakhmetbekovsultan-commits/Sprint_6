import pytest
import allure
from pages.main_page import MainPage
from data import ACCORDION_ANSWERS


@allure.feature("Вопросы о важном")
class TestImportantQuestions:

    @pytest.mark.parametrize("index, expected_answer", enumerate(ACCORDION_ANSWERS))
    @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном', вопрос №{index}")
    def test_accordion_question(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies_if_needed()
        
        # Кликаем по вопросу
        main_page.click_question(index)
        
        # Проверяем, что полученный текст совпадает с ожидаемым ответа
        answer_text = main_page.get_answer_text(index)
        assert answer_text == expected_answer, f"Текст ответа для вопроса {index} не совпадает!"
