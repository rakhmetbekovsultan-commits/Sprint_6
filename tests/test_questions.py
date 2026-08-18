import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestImportantQuestions:

    @pytest.mark.parametrize("index", range(8))
    @allure.title("Проверка выпадающего списка в разделе 'Вопросы о важном', вопрос №{index}")
    def test_accordion_question(self, driver, index):
        main_page = MainPage(driver)
        main_page.accept_cookies_if_needed()
        
        # Кликаем по вопросу
        main_page.click_question(index)
        
        # Проверяем, что текст ответа отображается и не пустой
        answer_text = main_page.get_answer_text(index)
        assert len(answer_text) > 0, f"Ответ на вопрос {index} пустой!"