import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.step("Открываем GitHub")
def open_github():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo_name}")
def search_repository(repo_name):
    s(".header-search-button").click()
    s("input[name='query-builder-test']").send_keys(repo_name)
    s("input[name='query-builder-test']").submit()


@allure.step("Переходим в репозиторий {repo_name}")
def open_repository(repo_name):
    s(by.link_text(repo_name)).click()


@allure.step("Открываем вкладку Issues")
def open_issues_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие задачи {issue_text}")
def check_issue_visibility(issue_text):
    s(by.text(issue_text)).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "kuznetsova")
@allure.feature("Задачи")
@allure.story("Просмотр Issues")
@allure.link("https://github.com", name="Testing")

def test_github_decor():
    repo_name = "AnastasiyaKZC/Homework_L10"
    issue_text = "Фича: “Добавить темную тему в UI.”"

    open_github()
    search_repository(repo_name)
    open_repository(repo_name)
    open_issues_tab()
    check_issue_visibility(issue_text)