import os
from aloe import world, before, after
from selenium import webdriver

@before.all
def open_shop():
    open_drivers()

@after.all
def close_shop():
    close_drivers()

def open_drivers():
    world.driver = get_chrome()
    world.driver.set_page_load_timeout(10)
    world.driver.implicitly_wait(10)
    world.driver.maximize_window()

def get_chrome():
    #driver = webdriver.Chrome(r'C:\Users\migue\Documents\Verificacion programas\chromedriver.exe')
    driver = webdriver.Chrome(r '~/proyectos/P4_Final_Verificacion/P3Verificacion/Apps/Web/test_automated/features/chromedriver')
    return driver

def close_drivers():
    if world.driver:
        world.driver.quit()
