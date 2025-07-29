from selenium.common import NoSuchElementException

from conftest import browser


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        """
        Метод, проверяющий существование элемента

        :param how: Как ищем элемент: id, css selector, xpath, etc
        :param what: Какой элемент ищем
        :return: Возвращает булевое значение, найден ли элемент
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True