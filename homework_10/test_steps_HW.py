import allure
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

def test_github():
    with allure.step("Открываем GitHub"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий AnastasiyaKZC/Homework_L10"):
        s(".header-search-button").click()
        s("input[name='query-builder-test']").send_keys("AnastasiyaKZC/Homework_L10")
        s("input[name='query-builder-test']").submit()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text("AnastasiyaKZC/Homework_L10")).click()

    with allure.step("Открываем вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие задачи 'Добавить темную тему в UI'"):
        s(by.text("Фича: “Добавить темную тему в UI.”")).should(be.visible)