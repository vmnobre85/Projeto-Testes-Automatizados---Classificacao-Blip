from behave import given, when, then
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

base_url = 'https://account.blip.ai/login'
google_menu = "google-icon"
element_user = "email"
element_key = "password"
element_send = "blip-login"


@given(u'que acesso a pagina inicial')
def step_impl(context):
    context.web.get(base_url)
    
@when(u'clico no google direciona ao login google e retorno a pagina inicial')
def step_impl(context):
    context.element_menu = context.web.find_element_by_class_name(google_menu)
    context.element_menu.click()
    sleep(2)
    context.web.get(base_url)
    sleep(2)
    
@when(u'testando elementos de usuário e senha')
def step_impl(context):
        context.element_user = context.web.find_element_by_id(element_user)
        sleep(2)
        context.element_user.click()
        sleep(2)
        context.element_user.send_keys('teste@teste.com')
        sleep(2)
        context.element_key = context.web.find_element_by_id(element_key)
        sleep(3)
        context.element_key.click()
        sleep(3)
        context.element_key.send_keys('teste12345')
        sleep(2)
        

@when(u'clico em login')
def step_impl(context):
        context.element_send = context.web.find_element_by_id(element_send)
        sleep(3)
        context.element_send.click()

@then(u'então login incorreto')
def step_impl(context):
    ...