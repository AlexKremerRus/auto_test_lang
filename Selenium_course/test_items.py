import pytest
from selenium import webdriver
import time
import math

link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestFindBtn:
    def test_find_bts_var_lang(self, browser):
        
        
        browser.get(link)
        browser.implicitly_wait(5) # ждет 5 скунд обновляясь каждые пол секунды
       
        btn=browser.find_element_by_class_name('btn-add-to-basket') # находит кнопку
        
        # browser.execute_script("return arguments[0].scrollIntoView(true);", btn) # скролит до кнопки, для удобства
        assert btn # проверка наличия кнопки
        # ждет 5 секунд чтобы пользователь мог оценить, что тест сработал и правильно выбран язык
        time.sleep(5)