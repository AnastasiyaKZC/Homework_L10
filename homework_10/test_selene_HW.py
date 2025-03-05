import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "kuznetsova")
@allure.feature("Задачи")
@allure.story("Просмотр Issues")
@allure.link("https://github.com", name="Testing")

def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click() # s() – сокращение от browser.element(), удобный способ работы с элементами на странице.
    s("input[name='query-builder-test']").send_keys("AnastasiyaKZC/Homework_L10")
    s("input[name='query-builder-test']").submit()

    s(by.link_text("AnastasiyaKZC/Homework_L10")).click()

    s("#issues-tab").click()

    s(by.text("Фича: “Добавить темную тему в UI.”")).should(be.visible)

