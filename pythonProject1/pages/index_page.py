from playwright.sync_api import Page
import config


class IndexPage:

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)



# Первая строка импортирует класс Page из playwright.
# Вторая строка импортирует созданный нами config.
# Пятая строка создает класс IndexPage.
# Седьмая строка создает метод, который и является необходимым нам шагом.#