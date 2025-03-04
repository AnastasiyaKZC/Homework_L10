import allure
from allure_commons.types import Severity


def test_no_labels():
    pass

# динамическое добавление меток. Динамический метод удобен, если метки формируются на основе данных во время теста (например, когда тесты параметризованы).
def test_dynamic_labels():
    allure.dynamic.tag("web")  # Добавляет тег "web" чтобы фильтровать тесты по категориям.
    allure.dynamic.severity(Severity.BLOCKER)  # Устанавливает уровень критичности как BLOCKER
    allure.dynamic.feature("Задачи в репозитории")  # Группирует тест по фиче "Задачи в репозитории"
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")  # Добавляет ссылку в отчет
    pass


# добавление меток через декораторы. Декораторы проще и удобнее, когда тестовые метки известны заранее.
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass