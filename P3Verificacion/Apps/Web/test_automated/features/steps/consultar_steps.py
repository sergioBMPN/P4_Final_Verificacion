from aloe import step, world
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('Open server')
def step_impl(step):
    world.driver.get("http://localhost:8000/Practica/contador")

@step('Write "([^"]*)"')
def step_impl(step, search_term):
    world.driver.find_element(By.NAME, "pagina").send_keys(search_term)

@step('Press "([^"]*)"')
def step_impl(step, button):
    world.driver.find_element(By.NAME, button).click()

@step('I see the result "([^"]*)"')
def step_impl(step, search_result):
    resultado = world.driver.find_element(By.NAME, "resultado").text
    assert_true(resultado, search_result)

@step('The url is deleted')
def step_impl(step):
    pagina = world.driver.find_element(By.NAME, "pagina").text
    assert not pagina

@step('Nothing happens')
def step_impl(step):
    pagina = world.driver.find_element(By.NAME, "pagina").text
    assert not pagina

@step('I see the db result "([^"]*)"')
def step_impl(step, resultado):
    res = world.driver.find_element(By.NAME, "base_datos").text
    assert_true(res, resultado)
