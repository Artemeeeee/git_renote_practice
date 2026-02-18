
import allure
from selene import browser, by, have, command


@allure.title("Заполнение регистрационной формы DemoQA")
def test_form_fill(setup_browser):
    browser = setup_browser
    with allure.step("Заполнить все поля формы"):
        browser.open('https://demoqa.com/')

        #ищем форму
        browser.element("//*[contains(text(), 'Forms')]").click()
        browser.element("//span[text()='Practice Form']").click()

        # Персональные данные
        browser.element('#firstName').type('Artem')
        browser.element('#lastName').type('Shmakov')
        browser.element('#userEmail').type('A.Shmakov@mail.ru')
        browser.element(by.text('Male')).click()
        browser.element('#userNumber').type('1234567890')

        # Дата рождения
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(by.text('2003')).click()
        browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
        browser.element('.react-datepicker__day--028').click()

        # Предметы и хобби
        browser.element('#subjectsInput').type('ma').press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('label[for="hobbies-checkbox-1"]').click()

        # Адрес
        browser.element('#currentAddress').type('Улица колотушкина 10')

        # Штат и город
        browser.element('#state').click()
        browser.element('#react-select-3-input').type('nc').press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type('d').press_enter()

        # Отправить
        browser.element('#submit').click()




    with allure.step("Проверить что данные отобразились корректно"):
        browser.all('.modal-body tr td:last-child').should(have.texts(
            'Artem Shmakov',
            'A.Shmakov@mail.ru',
            'Male',
            '1234567890',
            '28 January,2003',
            'Maths',
            'Sports',
            '',
            'Улица колотушкина 10',
            'NCR Delhi'
        ))


