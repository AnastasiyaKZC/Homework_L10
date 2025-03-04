import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

#РАЗМЕТКА АВТОТЕСТОВ
def test_dinamic_steps():
    with allure.step("Открываем главную страницу"): #разметка автотестов
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click() # s() – сокращение от browser.element(), удобный способ работы с элементами на странице.
        s("input[name='query-builder-test']").send_keys("eroshenkoam/allure-example")
        s("input[name='query-builder-test']").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие issue с номером 93"):
        s("//span[contains(text(), '93')]").should(be.visible)

# СТЕПОВЫЙ ПОДХОД с использованием декоратора ДЛЯ СЛОЖНОГО UI (для переиспользования)
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#93")


@allure.step("Открываем главную страницу") #аллюр декоратор
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()  # s() – сокращение от browser.element(), удобный способ работы с элементами на странице.
    s("input[name='query-builder-test']").send_keys("eroshenkoam/allure-example")
    s("input[name='query-builder-test']").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s("//span[contains(text(), '93')]").should(be.visible)
