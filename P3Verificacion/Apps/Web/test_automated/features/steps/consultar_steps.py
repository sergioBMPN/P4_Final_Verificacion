from aloe import step, world
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
import redis
import datetime

@step('Open server')
def step_impl(step):
    world.driver.get("http://localhost:8000/Practica/contador")

@step('Write "([^"]*)" y el dia actual')
def step_impl(step, search_term):
    world.driver.find_element(By.NAME, "pagina").send_keys(search_term)

    tiempo = datetime.datetime.now()
    dia = tiempo.day
    month = tiempo.month
    fecha_actual = str(dia) + "_" + str(month)

    world.driver.find_element(By.NAME, "dia_consultar").send_keys(fecha_actual)

@step('Press "([^"]*)"')
def step_impl(step, button):
    world.driver.find_element(By.NAME, button).click()

@step('Write "([^"]*)" y "([^"]*)"')
def step_impl(step, url, fecha):
    world.driver.find_element(By.NAME, "pagina").send_keys(url)
    world.driver.find_element(By.NAME, "dia_consultar").send_keys(fecha)

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
    bbdd = redis.Redis(host='localhost', port=6379)

    bbdd.flushdb()
    res = world.driver.find_element(By.NAME, "base_datos").text
    bbdd.flushdb()
    assert_true(res, resultado)
