from selene import browser, by, be
from selene.support.shared.jquery_style import s
import allure
from selene import support
import allure_commons

@allure.title('Проверка номера Issue')
def test_dynamic_steps():
    with allure.step("открываем главную страницу"):
        browser.open('https://github.com/')

    with allure.step("Ищем репозиторий"):
        s(".octicon-search").click()
        s(".FormControl-input").type('Artemeeeee/allure_practice')
        s(".FormControl-input").press_enter()
    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('Artemeeeee/allure_practice')).click()
    with allure.step("Открываем таб issues"):
        s('#issues-tab').click()
    with allure.step("Ищем issue с номером 1"):
        s(by.xpath("//span[normalize-space()='#1  ']")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository('Artemeeeee/allure_practice')
    go_to_repo_link('Artemeeeee/allure_practice')
    open_issues_tab()
    should_see_issue_number('1')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com/')

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".octicon-search").click()
    s(".FormControl-input").type(repo)
    s(".FormControl-input").press_enter()

@allure.step("Переходим по сслыке репозитория {repo}")
def go_to_repo_link(repo):
    s(by.link_text(repo)).click()

@allure.step("открываем tab issues")
def open_issues_tab():
    s('#issues-tab').click()

@allure.step("проверяем наличие issue с номером {number}")
def should_see_issue_number(number):
    #by.xpath(f"//span[normalize-space()='#{number}']").should(be.visible)
    browser.element(f"//a[contains(@href, '/issues/{number}')]").should(be.visible)










