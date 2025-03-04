from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click() # s() – сокращение от browser.element(), удобный способ работы с элементами на странице.
    s("input[name='query-builder-test']").send_keys("eroshenkoam/allure-example")
    s("input[name='query-builder-test']").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    # s("span.issue-item-module__defaultNumberDescription--GXzri").should(be.visible)
    # s(by.text("#93")).should(be.visible)
    s("//span[contains(text(), '93')]").should(be.visible)