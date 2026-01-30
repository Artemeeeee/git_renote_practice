from allure_commons.types import Severity
import allure


#@allure.title('Проверка номера Issue')
def test_dynamic_lables():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com/", name="Testing")
    pass


@allure.tag("web")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Задачи в репозитории")
@allure.story("авторизованный пользователь может создать задачу в репозитории ")
@allure.link("https://github.com/", name="Testing")
def test_decorator_lables():
    pass












