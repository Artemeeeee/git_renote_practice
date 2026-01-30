import json

import allure


def test_attachments():
    allure.attach("text content", name="текстовый файл", attachment_type=allure.attachment_type.TEXT)
    allure.attach("<h1>Hello world!</h1>", name="html", attachment_type=allure.attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second":2}), name = "Json", attachment_type=allure.attachment_type.JSON)

