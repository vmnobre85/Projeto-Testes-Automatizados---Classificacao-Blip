from selenium import webdriver

def before_all(context):
    context.web = webdriver.Chrome()

def driver_back(context):
    context_back = webdriver.Chrome.back()

def after_step(context, step):
    print()

def after_all(context):
    context.web.quit()


